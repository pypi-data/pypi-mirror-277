from collections.abc import Sequence
from typing import TypedDict


class Paginate(TypedDict):
    total: int
    page: int
    pages: int
    per_page: int
    prev: int | None
    next: int | None


class Pagination(TypedDict):
    items: Sequence
    pagination: Paginate
