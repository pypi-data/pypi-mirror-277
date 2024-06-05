import logging
from abc import ABC, abstractmethod
from copy import copy
from dataclasses import dataclass
from enum import Enum
from functools import wraps
from typing import Any, Optional
from uuid import UUID

from orca_common import ColumnName
from torch import nn

from orcalib.database import OrcaDatabase

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ProjectionMode(Enum):
    """
    Determines how the values from the memory should be "projected" into the models embedding space (i.e. what's the V in the attention mechanism QKV).

    Attributes:
        LABEL: Project the memory's label into the model embedding space.
        POSITIONAL: Project the memory's position (0...num_memories-1) into the model embedding space.
    """

    LABEL = 0
    POSITIONAL = 1


class ClassificationMode(Enum):
    """
    Determined how the final classification is performed.

    Attributes:
        DIRECT: Predicts directly into `num_classes` like a conventional classification model.
        MEMORY_BOUND: which uses memory binding to make the prediction (i.e. pick from the classes in the memories).
    """

    DIRECT = 0
    MEMORY_BOUND = 1


class DropExactMatchOption(Enum):
    # ALWAYS: Always drop exact matches from the results
    ALWAYS = "ALWAYS"
    # NEVER: Never drop exact matches from the results
    NEVER = "NEVER"
    # TRAINING_ONLY: Drop exact matches from the results only during training
    TRAINING_ONLY = "TRAINING_ONLY"
    # INFERENCE_ONLY: Drop exact matches from the results only during inference
    INFERENCE_ONLY = "INFERENCE_ONLY"


OrcaMetadataElement = str | int | float | bool
OrcaMetadataDict = dict[str, OrcaMetadataElement | list[OrcaMetadataElement] | None]


@dataclass
class CurateRunInfo:
    """Class for tracking settings of a curate run."""

    run_ids: list[int]
    model_id: str
    model_version: Optional[str]
    batch_size: int
    tags: set[str]
    metadata: OrcaMetadataDict
    seq_id: Optional[UUID]


class PostInitMixin(ABC):
    """Mixin class that adds an (abstract) post_init() and wraps descendent's __init__() to call it.

    NOTE: If PostInitMixin appears more than once in the inheritance chain, only the outermost class will run post_init().
    In other words, the post_init method will only be called once, after all other init methods have been called, even
    if there are multiple PostInitMixin classes in the inheritance chain.
    """

    def __init_subclass__(cls) -> None:
        """
        Initializes the subclass with the wrapped init method.  This is used to apply global settings to the model.
        This method is called when a subclass of OrcaModel is created.  It modifies the class directly by wrapping the
        __init__ method with custom logic.
        """
        super().__init_subclass__()

        old_init = cls.__init__

        def wrapped_init(self, *args, **kwargs):
            """
            The wrapped init function that initializes the model and applies global settings.
            :param args: The positional arguments.
            :param kwargs: The keyword arguments.
            """

            # We only want to run post_init once after all other init methods have been called,
            # so only the outermost class will run post_init.
            skip_post_init = getattr(self, "_skip_post_init", False)
            self._skip_post_init = True

            old_init(self, *args, **kwargs)
            if not skip_post_init:
                self.post_init()

        # Modify the class directly
        cls.__init__ = wrapped_init

    @abstractmethod
    def post_init(self) -> None:
        """
        Function that runs after the __init__ method.
        You can override this function to add new post-init behavior in derived classes.
        """
        ...


class PreForwardMixin(ABC):
    """Mixin class that adds an (abstract) pre_forward() and wraps descendent's forward() to call it before the
    original forward method.

    NOTE: This uses functools.wraps to wrap the forward method, so the original forward method's signature is preserved.
    """

    def __init_subclass__(cls) -> None:
        """
        Initializes the subclass with the wrapped forward method. This method is called when a subclass of OrcaModel is created.
        """
        super().__init_subclass__()

        forward_method = cls.forward

        @wraps(forward_method)
        def wrapped_forward(self, *args, **kwargs):
            self.pre_forward(*args, **kwargs)
            # Call the original forward method
            return forward_method(self, *args, **kwargs)

        cls.forward = wrapped_forward

    @abstractmethod
    def pre_forward(self, *args, **kwargs):
        """
        Function that runs before the forward method.
        You can override this function to add new pre-forward behavior in derived classes.
        """
        ...


class CurateSettings:
    """Class that holds the settings required for curating a model."""

    def __init__(
        self,
        curate_database: OrcaDatabase | str | None = None,
        model_id: Optional[str] = None,
        model_version: Optional[str] = None,
        metadata: Optional[OrcaMetadataDict] = None,
        curate_enabled: bool = False,
        tags: Optional[set[str]] = None,
    ):
        """Initializes the CurateSettings object.
        :param curate_database: The database to curate the model to.
        :param model_id: The model id to curate.
        :param model_version: The model version to curate.
        :param metadata: The metadata to attach to the model.
        :param curate_enabled: Whether the model should be curated.
        :param tags: The tags to attach to the model.
        """
        self.curate_database: OrcaDatabase | str | None = curate_database
        self.curate_enabled: bool = curate_enabled
        self.tags: set[str] = tags if tags is not None else set()
        self.metadata: OrcaMetadataDict = metadata if metadata is not None else {}
        self.model_id: Optional[str] = model_id
        self.model_version: Optional[str] = model_version

        self.seq_id: Optional[UUID] = None
        self.batch_size: Optional[int] = None
        self.last_batch_size: Optional[int] = None
        self.last_run_ids: Optional[list[int]] = None


class CurateSettingsMixin:
    """Mixin that adds curate settings to a class as self.curate_settings, then
    provides properties to access the individual settings.

    NOTE: This class is intended to be used with OrcaModule classes, and should not be
    used directly.
    """

    def __init__(
        self,
        curate_database: OrcaDatabase | str | None = None,
        model_id: Optional[str] = None,
        model_version: Optional[str] = None,
        metadata: Optional[OrcaMetadataDict] = None,
        curate_enabled: bool = False,
        tags: Optional[set[str]] = None,
    ):
        """Initializes the CurateSettings object.
        :param curate_database: The database to curate the model to.
        :param model_id: The model id to associate with curate runs.
        :param model_version: The model version to associate with curate runs.
        :param metadata: The metadata to attach to curate runs.
        :param curate_enabled: Whether the model should be curated.
        :param tags: The tags to attach to the model.
        """
        self._curate_settings = CurateSettings(
            curate_database=curate_database,
            model_id=model_id,
            model_version=model_version,
            metadata=metadata,
            tags=tags,
        )
        self.curate_layer_name: Optional[str] = None
        self.curate_enabled = curate_enabled

    @property
    def curate_database(self) -> OrcaDatabase | None:
        return self._curate_settings.curate_database

    @curate_database.setter
    def curate_database(self, value: OrcaDatabase | str | None) -> None:
        if isinstance(value, str):
            self._curate_settings.curate_database = value
        elif value is None or isinstance(value, OrcaDatabase):
            self._curate_settings.curate_database = value.name
        else:
            raise ValueError(f"Database is wrong type: {type(value)}. Expected str or OrcaDatabase")

    @property
    def curate_model_id(self) -> str | None:
        return self._curate_settings.model_id

    @curate_model_id.setter
    def curate_model_id(self, value: str | None) -> None:
        self._curate_settings.model_id = value

    @property
    def curate_model_version(self) -> str | None:
        return self._curate_settings.model_version

    @curate_model_version.setter
    def curate_model_version(self, value: str | None) -> None:
        self._curate_settings.model_version = value

    @property
    def curate_metadata(self) -> OrcaMetadataDict:
        return self._curate_settings.metadata

    @curate_metadata.setter
    def curate_metadata(self, value: OrcaMetadataDict) -> None:
        for k, v in value.items():
            assert isinstance(v, (str, int, float, bool, list)), f"Metadata value must be a simple type, not {type(v)}"
            if isinstance(v, list):
                assert all(
                    isinstance(x, (str, int, float, bool)) for x in v
                ), f"Metadata value must be a simple type, not {type(v)}"
        self._curate_settings.metadata = value

    @property
    def curate_tags(self) -> set[str]:
        return self._curate_settings.tags

    @curate_tags.setter
    def curate_tags(self, value: set[str]) -> None:
        assert isinstance(value, set), f"Tags must be a set, not {type(value)}"
        self._curate_settings.tags = value

    @property
    def curate_seq_id(self) -> UUID | None:
        return self._curate_settings.seq_id

    @curate_seq_id.setter
    def curate_seq_id(self, value: UUID | None) -> None:
        self._curate_settings.seq_id = value

    @property
    def curate_batch_size(self) -> int | None:
        return self._curate_settings.batch_size

    @curate_batch_size.setter
    def curate_batch_size(self, value: int | None) -> None:
        self._curate_settings.batch_size = value

    @property
    def last_curate_batch_size(self) -> int | None:
        return self._curate_settings.last_batch_size

    @last_curate_batch_size.setter
    def last_curate_batch_size(self, value: int | None) -> None:
        self._curate_settings.last_batch_size = value

    @property
    def last_curate_run_ids(self) -> list[int] | None:
        return self._curate_settings.last_run_ids

    @last_curate_run_ids.setter
    def last_curate_run_ids(self, value: list[int] | None) -> None:
        self._curate_settings.last_run_ids = value

    @property
    def curate_database_instance(self) -> OrcaDatabase | None:
        db = self._curate_settings.curate_database
        if db is None:
            return None
        elif isinstance(db, str):
            return OrcaDatabase(db)
        elif isinstance(db, OrcaDatabase):
            return db
        else:
            raise ValueError(f"Value of curate database ({db}) is wrong type: {type(db)}")

    @curate_database_instance.setter
    def curate_database_instance(self, value: OrcaDatabase | str | None) -> None:
        if isinstance(value, str):
            self._curate_settings.curate_database = value
        elif value is None or isinstance(value, OrcaDatabase):
            self._curate_settings.curate_database = value.name
        else:
            ValueError(f"Curate Database is wrong type: {type(value)}. Expected str or OrcaDatabase")

    def last_curate_run_info(self):
        assert (
            self.curate_model_id is not None
            and self.last_curate_batch_size is not None
            and self.last_curate_run_ids is not None
        ), f"It seems there is no last curate run on this model: {self.curate_model_id}, {self.last_curate_batch_size}, {self.last_curate_run_ids}"
        return CurateRunInfo(
            run_ids=self.last_curate_run_ids,
            batch_size=self.last_curate_batch_size,
            model_id=self.curate_model_id,
            model_version=self.curate_model_version,
            tags=self.curate_tags,
            metadata=self.curate_metadata,
            seq_id=self.curate_seq_id,
        )


@dataclass
class LookupSettings:
    """Class that holds the settings required for lookup in the model.

    NOTE: This class is intended to be used with OrcaModule classes, and should not be used directly.
    """

    lookup_database: OrcaDatabase | str | None = None
    memory_index_name: Optional[str] = None
    lookup_column_names: Optional[list[str]] = None
    num_memories: Optional[int] = None
    drop_exact_match: Optional[DropExactMatchOption] = DropExactMatchOption.NEVER
    exact_match_threshold: Optional[float] = None
    shuffle_memories: Optional[bool] = None
    # If True, the number of memories will not be changed once set
    freeze_num_memories: bool = False

    def __or__(self, other: "LookupSettings") -> "LookupSettings":
        """Merges two LookupSettings objects, preferring the values in self if they are set."""
        return LookupSettings(
            lookup_database=self.lookup_database if self.lookup_database is not None else other.lookup_database,
            memory_index_name=self.memory_index_name if self.memory_index_name is not None else other.memory_index_name,
            lookup_column_names=(
                self.lookup_column_names if self.lookup_column_names is not None else other.lookup_column_names
            ),
            num_memories=self.num_memories if self.num_memories is not None else other.num_memories,
            drop_exact_match=self.drop_exact_match if self.drop_exact_match is not None else other.drop_exact_match,
            exact_match_threshold=self.exact_match_threshold
            if self.exact_match_threshold is not None
            else other.exact_match_threshold,
            shuffle_memories=self.shuffle_memories if self.shuffle_memories is not None else other.shuffle_memories,
        )


class LookupSettingsMixin:
    """Mixin that adds lookup settings to a class as self.lookup_settings, then provides properties to
    access the individual settings.

    NOTE: This class is intended to be used with OrcaModule classes, and should not be used directly.
    """

    def __init__(
        self,
        lookup_database: OrcaDatabase | str | None = None,
        memory_index_name: Optional[str] = None,
        lookup_column_names: Optional[list[str]] = None,
        num_memories: Optional[int] = None,
        drop_exact_match: Optional[DropExactMatchOption] = None,
        exact_match_threshold: Optional[float] = None,
        shuffle_memories: Optional[bool] = None,
        freeze_num_memories: bool = False,
        propagate_lookup_settings: bool = True,
    ):
        self._orca_lookup_settings = LookupSettings(
            lookup_database=lookup_database,
            memory_index_name=memory_index_name,
            lookup_column_names=lookup_column_names,
            num_memories=num_memories,
            drop_exact_match=drop_exact_match,
            exact_match_threshold=exact_match_threshold,
            shuffle_memories=shuffle_memories,
            freeze_num_memories=freeze_num_memories,
        )
        self.propagate_lookup_settings = propagate_lookup_settings
        self._inherited_orca_lookup_settings = LookupSettings()

    def _propagate_lookup_settings(self) -> None:
        """Propagates lookup settings to the nearest OrcaLookupModules through each of its children.

        NOTE: You should not call this method directly. It is called automatically when lookup settings are updated.
        """
        from orcalib.orca_torch import OrcaLookupModule

        assert isinstance(
            self, OrcaLookupModule
        ), "_propagate_lookup_settings() should only be called from OrcaLookupModule"

        for module in self.get_orca_modules_recursively(max_depth=1, include_self=False, filter_type=OrcaLookupModule):
            if self.propagate_lookup_settings:
                module._inherited_orca_lookup_settings = (
                    self._orca_lookup_settings | self._inherited_orca_lookup_settings
                )
            module._propagate_lookup_settings()

    def update_lookup_settings(
        self,
        database: OrcaDatabase | str | None = None,
        memory_index_name: Optional[str] = None,
        lookup_column_names: Optional[list[str]] = None,
        num_memories: Optional[int] = None,
        drop_exact_match: Optional[DropExactMatchOption] = None,
        exact_match_threshold: Optional[float] = None,
        shuffle_memories: Optional[bool] = None,
    ):
        self._orca_lookup_settings |= LookupSettings(
            lookup_database=database,
            memory_index_name=memory_index_name,
            lookup_column_names=lookup_column_names,
            num_memories=num_memories,
            drop_exact_match=drop_exact_match,
            exact_match_threshold=exact_match_threshold,
            shuffle_memories=shuffle_memories,
        )
        self._propagate_lookup_settings()

    @property
    def lookup_database(self) -> OrcaDatabase | None:
        return self._orca_lookup_settings.lookup_database or self._inherited_orca_lookup_settings.lookup_database

    @lookup_database.setter
    def lookup_database(self, value: OrcaDatabase | str | None) -> None:
        if value is None:
            self._orca_lookup_settings.lookup_database = None
        elif isinstance(value, str):
            self._orca_lookup_settings.lookup_database = value
        elif isinstance(value, OrcaDatabase):
            self._orca_lookup_settings.lookup_database = value.name
        else:
            raise ValueError(f"Lookup Database is wrong type: {type(value)}. Expected str or OrcaDatabase")
        self._propagate_lookup_settings()

    @property
    def lookup_database_instance(self) -> OrcaDatabase | None:
        db = self._orca_lookup_settings.lookup_database or self._inherited_orca_lookup_settings.lookup_database
        if db is None:
            return None
        elif isinstance(db, str):
            return OrcaDatabase(db)
        elif isinstance(db, OrcaDatabase):
            return db
        else:
            raise ValueError(f"Value of lookup database ({db}) is wrong type: {type(db)}")

    @lookup_database_instance.setter
    def lookup_database_instance(self, value: OrcaDatabase | str | None) -> None:
        if isinstance(value, str):
            self._orca_lookup_settings.lookup_database = value
        elif value is None or isinstance(value, OrcaDatabase):
            self._orca_lookup_settings.lookup_database = value.name
        else:
            raise ValueError(f"Database is wrong type: {type(value)}. Expected str or OrcaDatabase")
        self._propagate_lookup_settings()

    @property
    def memory_index_name(self) -> str | None:
        return self._orca_lookup_settings.memory_index_name or self._inherited_orca_lookup_settings.memory_index_name

    @memory_index_name.setter
    def memory_index_name(self, value: str | None) -> None:
        self._orca_lookup_settings.memory_index_name = value
        self._propagate_lookup_settings()

    @property
    def lookup_column_names(self) -> list[str] | None:
        return (
            self._orca_lookup_settings.lookup_column_names or self._inherited_orca_lookup_settings.lookup_column_names
        )

    @lookup_column_names.setter
    def lookup_column_names(self, value: list[str] | None) -> None:
        self._orca_lookup_settings.lookup_column_names = value
        self._propagate_lookup_settings()

    @property
    def num_memories(self) -> int | None:
        return self._orca_lookup_settings.num_memories or self._inherited_orca_lookup_settings.num_memories

    @num_memories.setter
    def num_memories(self, value: int | None) -> None:
        if self._orca_lookup_settings.freeze_num_memories and self._orca_lookup_settings.num_memories is not None:
            raise ValueError(
                "num_memories is frozen and cannot be changed. This is a safety feature to prevent accidental changes."
            )
        self._orca_lookup_settings.num_memories = value
        self._propagate_lookup_settings()

    @property
    def drop_exact_match(self) -> DropExactMatchOption:
        return self._orca_lookup_settings.drop_exact_match or self._inherited_orca_lookup_settings.drop_exact_match

    @drop_exact_match.setter
    def drop_exact_match(self, value: DropExactMatchOption) -> None:
        self._orca_lookup_settings.drop_exact_match = value
        self._propagate_lookup_settings()

    @property
    def exact_match_threshold(self) -> float:
        return (
            self._orca_lookup_settings.exact_match_threshold
            or self._inherited_orca_lookup_settings.exact_match_threshold
        )

    @exact_match_threshold.setter
    def exact_match_threshold(self, value: float) -> None:
        self._orca_lookup_settings.exact_match_threshold = value
        self._propagate_lookup_settings()

    @property
    def shuffle_memories(self) -> bool:
        return self._orca_lookup_settings.shuffle_memories or self._inherited_orca_lookup_settings.shuffle_memories

    @shuffle_memories.setter
    def shuffle_memories(self, value: bool) -> None:
        self._orca_lookup_settings.shuffle_memories = value
        self._propagate_lookup_settings()


class LabelColumnNameMixin:
    """Mixin that lets the user set a label column for lookup instead of requiring them to set the lookup column names directly.
    It can be mixed with OrcaModel or OrcaLookupModule classes.

    This is useful when the user wants the lookup columns to be ["$embedding", label_column_name]. The label_column_name
    property handles updates to lookup_column_names automatically.

    NOTE: Make sure to set self.label_column_name AFTER calling super().__init__(...) in derived modules/models.
    """

    def __init__(self):
        self._label_column_name = None

    @property
    def label_column_name(self) -> ColumnName:
        if self.lookup_column_names and len(self.lookup_column_names) == 2:
            return self.lookup_column_names[1]
        return self._label_column_name

    @label_column_name.setter
    def label_column_name(self, value: ColumnName):
        self._label_column_name = value
        self.lookup_column_names = ["$embedding", value] if value else None
