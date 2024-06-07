from __future__ import annotations

from functools import partial
from pathlib import Path, PurePath
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    List,
    Sequence,
    cast,
)
from uuid import UUID

from advanced_alchemy.exceptions import AdvancedAlchemyError
from advanced_alchemy.filters import FilterTypes, LimitOffset
from advanced_alchemy.repository.typing import ModelOrRowMappingT
from advanced_alchemy.service.pagination import OffsetPagination

if TYPE_CHECKING:
    from sqlalchemy import ColumnElement

    from advanced_alchemy.service.typing import FilterTypeT, ModelDTOT

try:
    from msgspec import Struct, convert  # pyright: ignore[reportAssignmentType]
except ImportError:  # pragma: nocover

    class Struct:  # type: ignore[no-redef]
        """Placeholder Implementation"""

    def convert(*args: Any, **kwargs: Any) -> Any:  # type: ignore[no-redef] # noqa: ARG001
        """Placeholder implementation"""
        return {}


try:
    from pydantic import BaseModel  # pyright: ignore[reportAssignmentType]
    from pydantic.type_adapter import TypeAdapter  # pyright: ignore[reportAssignmentType]
except ImportError:  # pragma: nocover

    class BaseModel:  # type: ignore[no-redef]
        """Placeholder Implementation"""

    class TypeAdapter:  # type: ignore[no-redef]
        """Placeholder Implementation"""


def _default_deserializer(
    target_type: Any,
    value: Any,
    type_decoders: Sequence[tuple[Callable[[Any], bool], Callable[[Any, Any], Any]]] | None = None,
) -> Any:  # pragma: no cover
    """Transform values non-natively supported by ``msgspec``

    Args:
        target_type: Encountered type
        value: Value to coerce
        type_decoders: Optional sequence of type decoders

    Returns:
        A ``msgspec``-supported type
    """

    if isinstance(value, target_type):
        return value

    if type_decoders:
        for predicate, decoder in type_decoders:
            if predicate(target_type):
                return decoder(target_type, value)

    if issubclass(target_type, (Path, PurePath, UUID)):
        return target_type(value)

    msg = f"Unsupported type: {type(value)!r}"
    raise TypeError(msg)


def _find_filter(
    filter_type: type[FilterTypeT],
    filters: Sequence[FilterTypes | ColumnElement[bool]] | Sequence[FilterTypes],
) -> FilterTypeT | None:
    """Get the filter specified by filter type from the filters.

    Args:
        filter_type: The type of filter to find.
        filters: filter types to apply to the query

    Returns:
        The match filter instance or None
    """
    return next(
        (cast("FilterTypeT | None", filter_) for filter_ in filters if isinstance(filter_, filter_type)),
        None,
    )


def to_schema(
    data: ModelOrRowMappingT | Sequence[ModelOrRowMappingT],
    total: int | None = None,
    filters: Sequence[FilterTypes | ColumnElement[bool]] | Sequence[FilterTypes] | None = None,
    schema_type: type[ModelDTOT] | None = None,
) -> ModelOrRowMappingT | OffsetPagination[ModelOrRowMappingT] | ModelDTOT | OffsetPagination[ModelDTOT]:
    if filters is None:
        filters = []
    if schema_type is None:
        if not issubclass(type(data), Sequence):
            return cast("ModelOrRowMappingT", data)
        limit_offset = _find_filter(LimitOffset, filters=filters)
        total = total or len(data)  # type: ignore[arg-type]
        limit_offset = limit_offset if limit_offset is not None else LimitOffset(limit=len(data), offset=0)  # type: ignore[arg-type]
        return OffsetPagination[ModelOrRowMappingT](
            items=cast("List[ModelOrRowMappingT]", data),
            limit=limit_offset.limit,
            offset=limit_offset.offset,
            total=total,
        )
    if issubclass(schema_type, Struct):
        if not isinstance(data, Sequence):
            return convert(  # type: ignore  # noqa: PGH003
                obj=data,
                type=schema_type,
                from_attributes=True,
                dec_hook=partial(
                    _default_deserializer,
                    type_decoders=[
                        (lambda x: x is UUID, lambda t, v: t(v.hex)),
                    ],
                ),
            )
        limit_offset = _find_filter(LimitOffset, filters=filters)
        total = total or len(data)
        limit_offset = limit_offset if limit_offset is not None else LimitOffset(limit=len(data), offset=0)
        return OffsetPagination[schema_type](  # type: ignore[valid-type]
            items=convert(
                obj=data,
                type=List[schema_type],  # type: ignore[valid-type]
                from_attributes=True,
                dec_hook=partial(
                    _default_deserializer,
                    type_decoders=[
                        (lambda x: x is UUID, lambda t, v: t(v.hex)),
                    ],
                ),
            ),
            limit=limit_offset.limit,
            offset=limit_offset.offset,
            total=total,
        )

    if issubclass(schema_type, BaseModel):
        if not isinstance(data, Sequence):
            return TypeAdapter(schema_type).validate_python(data, from_attributes=True)  # type: ignore[return-value] # pyright: ignore[reportUnknownVariableType,reportUnknownMemberType,reportAttributeAccessIssue,reportCallIssue]
        limit_offset = _find_filter(LimitOffset, filters=filters)
        total = total if total else len(data)
        limit_offset = limit_offset if limit_offset is not None else LimitOffset(limit=len(data), offset=0)
        return OffsetPagination[schema_type](  # type: ignore[valid-type]
            items=TypeAdapter(List[schema_type]).validate_python(data, from_attributes=True),  # type: ignore[valid-type]
            limit=limit_offset.limit,
            offset=limit_offset.offset,
            total=total,
        )
    msg = "`schema_type` should be a valid Pydantic or Msgspec schema"
    raise AdvancedAlchemyError(msg)
