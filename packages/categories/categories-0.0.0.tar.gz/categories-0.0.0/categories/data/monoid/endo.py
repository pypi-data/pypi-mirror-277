from __future__ import annotations

from typing import TypeVar

from categories.data.endo import Endo
from categories.data.function import id
from categories.data.semigroup import SemigroupEndo

from . import Monoid

__all__ = (
    'MonoidEndo',
)


a = TypeVar('a')


class MonoidEndo(SemigroupEndo[a], Monoid[Endo[a]]):
    def empty(self, /) -> Endo[a]:
        return Endo(id)