from __future__ import annotations

from typing import TypeVar

from categories.data.functor import FunctorIO
from categories.type import IO, Lambda

from . import Applicative

__all__ = (
    'ApplicativeIO',
)


a = TypeVar('a')

b = TypeVar('b')


class ApplicativeIO(FunctorIO, Applicative[IO]):
    async def pure(self, x : a, /) -> a:
        return x

    async def apply(self, m : IO[Lambda[a, b]], m_ : IO[a], /) -> b:
        match (await m, await m_):
            case f, x:
                return f(x)