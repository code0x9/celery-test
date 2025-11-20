from typing import Any, Protocol, TypeVar

_T = TypeVar("_T")


class SupportsAdd(Protocol[_T]):
    def __add__(self, other: _T) -> _T: ...


AddableT = TypeVar("AddableT", bound=SupportsAdd[Any])
