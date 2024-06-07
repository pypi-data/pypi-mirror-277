from __future__ import annotations

from functools import reduce
from itertools import repeat
from typing import TypeVar

from categories.data.endo import Endo
from categories.data.function import o
from categories.type import data

from . import Semigroup

__all__ = (
    'SemigroupEndo',
)


a = TypeVar('a')


class SemigroupEndo(Semigroup[Endo[a]]):
    def append(self, x : Endo[a], y : Endo[a], /) -> Endo[a]:
        match (x, y):
            case Endo(f), Endo(g):
                return Endo(o(f, g))

    def times(self, n : int, x : Endo[a], /) -> Endo[a]:
        match x:
            case Endo(f):
                return Endo(reduce(o, repeat(f, n)))