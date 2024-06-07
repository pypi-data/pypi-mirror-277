from __future__ import annotations

from typing import TypeVar

from categories.type import IO, Lambda

from . import Functor

__all__ = (
    'FunctorIO',
)


a = TypeVar('a')

b = TypeVar('b')


class FunctorIO(Functor[IO]):
    async def fmap(self, f : Lambda[a, b], m : IO[a], /) -> b:
        match await m:
            case x:
                return f(x)