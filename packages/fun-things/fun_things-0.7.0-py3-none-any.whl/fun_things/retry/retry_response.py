from typing import Generic, NamedTuple, TypeVar

TValue = TypeVar("TValue")


class RetryResponse(NamedTuple, Generic[TValue]):
    value: TValue
    ok: bool
    error: Exception
