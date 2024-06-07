from __future__ import annotations

from functools import reduce
from typing import TypeVar

from categories.data.semigroup import Semigroup
from categories.type import typeclass

__all__ = (
    'Monoid',
)


a = TypeVar('a')


class Monoid(Semigroup[a], typeclass[a]):
    def empty(self, /) -> a:
        return self.concat([])

    def concat(self, xs : list[a], /) -> a:
        return reduce(self.append, xs, self.empty())