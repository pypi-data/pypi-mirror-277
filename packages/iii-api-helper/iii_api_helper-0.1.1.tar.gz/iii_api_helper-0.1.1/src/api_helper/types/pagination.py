from collections.abc import Sequence
from typing import Generic
from typing import TypeVar

from typing_extensions import TypedDict

T = TypeVar("T")


class Paginate(TypedDict):
    total: int
    page: int
    pages: int
    per_page: int
    prev: int | None
    next: int | None


class Pagination(TypedDict, Generic[T]):
    items: Sequence[T]
    pagination: Paginate
