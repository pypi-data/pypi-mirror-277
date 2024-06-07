from __future__ import annotations

from typing import TypeVar

from categories.type import Lambda, hkt, typeclass

__all__ = (
    'Functor',
)


a = TypeVar('a')

b = TypeVar('b')

f = TypeVar('f')


class Functor(typeclass[f]):
    def fmap(self, f : Lambda[a, b], x : hkt[f, a], /) -> hkt[f, b]: ...