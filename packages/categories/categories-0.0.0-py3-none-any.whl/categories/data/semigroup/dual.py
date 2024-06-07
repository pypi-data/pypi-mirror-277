from __future__ import annotations

from typing import TypeVar

from categories.data.dual import Dual
from categories.type import data

from . import Semigroup

__all__ = (
    'SemigroupDual',
)


a = TypeVar('a')


@data(frozen=True)
class SemigroupDual(Semigroup[Dual[a]]):
    inst : Semigroup[a]

    def append(self, x : Dual[a], y : Dual[a], /) -> Dual[a]:
        match (self, x, y):
            case SemigroupDual(inst), Dual(x_), Dual(y_):
                return Dual(inst.append(y_, x_))

    def times(self, n : int, x : Dual[a], /) -> Dual[a]:
        match (self, x):
            case SemigroupDual(inst), Dual(x_):
                return Dual(inst.times(n, x_))