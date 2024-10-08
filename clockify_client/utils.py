from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, TypeVar

if TYPE_CHECKING:
    from typing import ParamSpec

    P = ParamSpec("P")
    T = TypeVar("T")


class Singleton(type):
    """Singleton metaclass."""

    _instances: ClassVar[dict] = {}

    def __call__(cls, *args: P.args, **kwargs: P.kwargs) -> Singleton:
        """Create **singleton** instead of normal instance when used as metaclass."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
