from __future__ import annotations

from typing import TypeVar

from categories.control.applicative import Applicative
from categories.type import hkt, typeclass

__all__ = (
    'Alternative',
)


a = TypeVar('a')

b = TypeVar('b')

f = TypeVar('f')


class Alternative(Applicative[f], typeclass[f]):
    def empty(self, /) -> hkt[f, a]: ...

    def alt(self, x : hkt[f, a], y : hkt[f, a], /) -> hkt[f, a]: ...

    def some(self, v : hkt[f, a], /) -> hkt[f, list[a]]:
        return self.apply(self.fmap(lambda x, /: lambda xs, /: [x, *xs], v), self.many(v))

    def many(self, v : hkt[f, a], /) -> hkt[f, list[a]]:
        return self.alt(self.some(v), self.pure([]))