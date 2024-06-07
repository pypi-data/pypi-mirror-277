from __future__ import annotations

from typing import TypeVar

from categories.data.functor import Functor
from categories.type import Lambda, hkt, typeclass

__all__ = (
    'Applicative',
)


a = TypeVar('a')

b = TypeVar('b')

f = TypeVar('f')


class Applicative(Functor[f], typeclass[f]):
    def pure(self, x : a, /) -> hkt[f, a]: ...

    def apply(self, f : hkt[f, Lambda[a, b]], x : hkt[f, a], /) -> hkt[f, b]: ...