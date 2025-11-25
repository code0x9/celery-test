from typing import Any, Protocol, TypeVar, runtime_checkable

_T = TypeVar("_T")


@runtime_checkable
class SupportsAdd(Protocol[_T]):
    def __add__(self, other: _T) -> _T: ...


AddableT = TypeVar("AddableT", bound=SupportsAdd[Any])
