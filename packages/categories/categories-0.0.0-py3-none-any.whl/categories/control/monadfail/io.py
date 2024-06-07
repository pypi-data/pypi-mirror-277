from __future__ import annotations

from typing import TypeVar

from categories.control.monad import MonadIO
from categories.type import IO

from . import MonadFail

__all__ = (
    'MonadFailIO',
)


a = TypeVar('a')


class MonadFailIO(MonadIO, MonadFail[IO]):
    async def fail(self, x : str, /) -> a:
        raise Exception(x)