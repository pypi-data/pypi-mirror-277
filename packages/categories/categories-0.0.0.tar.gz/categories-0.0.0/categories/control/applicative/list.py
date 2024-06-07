from __future__ import annotations

from typing import TypeVar

from categories.data.functor import FunctorList
from categories.type import Lambda

from . import Applicative

__all__ = (
    'ApplicativeList',
)


a = TypeVar('a')

b = TypeVar('b')


class ApplicativeList(FunctorList, Applicative[list]):
    def pure(self, x : a, /) -> list[a]:
        return [x]

    def apply(self, fs : list[Lambda[a, b]], xs : list[a], /) -> list[b]:
        return [f(x) for f in fs for x in xs]