from __future__ import annotations

from typing import TypeVar

from categories.control.alternative import Alternative
from categories.control.monad import Monad
from categories.type import hkt, typeclass

__all__ = (
    'MonadPlus',
)


a = TypeVar('a')

m = TypeVar('m')


class MonadPlus(Alternative[m], Monad[m], typeclass[m]):
    def zero(self, /) -> hkt[m, a]:
        return self.empty()

    def plus(self, x : hkt[m, a], y : hkt[m, a], /) -> hkt[m, a]:
        return self.alt(x, y)