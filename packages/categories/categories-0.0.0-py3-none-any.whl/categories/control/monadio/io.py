from __future__ import annotations

from typing import TypeVar

from categories.type import IO

from . import MonadIO

__all__ = (
    'MonadIOIO',
)


a = TypeVar('a')


class MonadIOIO(MonadIO[IO]):
    async def liftIO(self, m : IO[a], /) -> a:
        return await m