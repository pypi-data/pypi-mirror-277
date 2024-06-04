from __future__ import annotations

__all__ = ("Middleware",)

from typing import TYPE_CHECKING
from typing import Any
from typing import Generic
from typing import TypeVar

if TYPE_CHECKING:
    from collections.abc import Callable

T = TypeVar("T")


class Middleware(Generic[T]):

    def __init__(
        self,
        obj: Callable[[T], T],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self.obj = obj
        self.args = args
        self.kwargs = kwargs

    def __call__(self, obj: T) -> T:
        return self.obj(obj, *self.args, **self.kwargs)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Middleware) and (  # yapf: disable
            other is self or (
                other.obj is self.obj
                and other.args == self.args
                and other.kwargs == self.kwargs
            )
        )
