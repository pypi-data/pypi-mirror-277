from __future__ import annotations

from typing import TypeVar

from categories.data.dual import Dual
from categories.data.semigroup import SemigroupDual
from categories.type import data

from . import Monoid

__all__ = (
    'MonoidDual',
)


a = TypeVar('a')


@data(frozen=True)
class MonoidDual(SemigroupDual[a], Monoid[Dual[a]]):
    inst : Monoid[a]

    def empty(self, /) -> Dual[a]:
        match self:
            case MonoidDual(inst):
                return Dual(inst.empty())