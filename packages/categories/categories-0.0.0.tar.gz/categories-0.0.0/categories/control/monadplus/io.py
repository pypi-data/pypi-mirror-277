from __future__ import annotations

from typing import TypeVar

from categories.control.alternative import AlternativeIO
from categories.control.monad import MonadIO
from categories.type import IO

from . import MonadPlus

__all__ = (
    'MonadPlusIO',
)


a = TypeVar('a')


class MonadPlusIO(AlternativeIO, MonadIO, MonadPlus[IO]):
    async def zero(self, /) -> a:
        raise Exception('mzero')

    async def plus(self, m : IO[a], m_ : IO[a], /) -> a:
        try:
            return await m
        except BaseException:
            return await m_