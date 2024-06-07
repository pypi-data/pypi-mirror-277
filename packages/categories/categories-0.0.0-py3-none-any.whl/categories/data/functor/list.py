from __future__ import annotations

from typing import TypeVar

from categories.type import Lambda

from . import Functor

__all__ = (
    'FunctorList',
)


a = TypeVar('a')

b = TypeVar('b')


class FunctorList(Functor[list]):
    def fmap(self, f : Lambda[a, b], xs : list[a], /) -> list[b]:
        return [f(x) for x in xs]