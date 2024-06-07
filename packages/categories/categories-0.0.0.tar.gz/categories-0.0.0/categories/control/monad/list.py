from __future__ import annotations

from typing import TypeVar

from categories.control.applicative import ApplicativeList
from categories.type import Lambda

from . import Monad

__all__ = (
    'MonadList',
)


a = TypeVar('a')

b = TypeVar('b')


class MonadList(ApplicativeList, Monad[list]):
    def bind(self, xs : list[a], f : Lambda[a, list[b]], /) -> list[b]:
        return [y for x in xs for y in f(x)]