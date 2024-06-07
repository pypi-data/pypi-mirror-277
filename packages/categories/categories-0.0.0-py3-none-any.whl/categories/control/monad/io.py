from __future__ import annotations

from typing import TypeVar

from categories.control.applicative import ApplicativeIO
from categories.type import IO, Lambda

from . import Monad

__all__ = (
    'MonadIO',
)


a = TypeVar('a')

b = TypeVar('b')


class MonadIO(ApplicativeIO, Monad[IO]):
    async def bind(self, m : IO[a], k : Lambda[a, IO[b]], /) -> b:
        match await m:
            case x:
                return await k(x)