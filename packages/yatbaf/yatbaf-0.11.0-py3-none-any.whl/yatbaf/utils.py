from __future__ import annotations

__all__ = (
    "parse_command",
    "parse_command_args",
    "extract_bot_id",
    "wrap_middleware",
    "ensure_unique",
)

from typing import TYPE_CHECKING
from typing import TypeVar

from .exceptions import InvalidTokenError

if TYPE_CHECKING:
    from collections.abc import Callable
    from collections.abc import Iterable

    from .middleware import Middleware

    F = TypeVar("F", bound=Callable)
else:
    F = TypeVar("F")

T = TypeVar("T")


def parse_command(text: str) -> str | None:
    """Parse bot command.

    :param text: Message text.
    """

    if not text.startswith("/") or text == "/":
        return None

    return text.removeprefix("/").split("@")[0].split(maxsplit=1)[0].lower()


def parse_command_args(text: str) -> list[str]:
    """Parse command args.

    :param text: Message with command.
    """

    return sp[-1].split() if len(sp := text.split(maxsplit=1)) == 2 else []


def extract_bot_id(token: str) -> int:
    try:
        return int(token.split(":")[0])
    except ValueError:
        raise InvalidTokenError() from None


def ensure_unique(objs: Iterable[T]) -> list[T]:
    tmp: list[T] = []

    for obj in objs:
        if obj not in tmp:
            tmp.append(obj)
    return tmp


def wrap_middleware(
    fn: F,
    middleware: list[Middleware[F] | Callable[[F], F]],
) -> F:
    result = fn
    for obj in reversed(middleware):
        result = obj(result)
    return result
