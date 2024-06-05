from datetime import datetime
from typing import Generic
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    data: T
    datetime: datetime


class ErrorResponse(BaseModel, Generic[T]):
    error: T
    datetime: datetime
