from __future__ import annotations

from typing import TypeVar

from categories.control.applicative import Applicative
from categories.type import Lambda, hkt, typeclass

__all__ = (
    'Monad',
)


a = TypeVar('a')

b = TypeVar('b')

m = TypeVar('m')


class Monad(Applicative[m], typeclass[m]):
    def bind(self, m : hkt[m, a], k : Lambda[a, hkt[m, b]], /) -> hkt[m, b]: ...