from __future__ import annotations

from typing import TypeVar

from categories.control.category import Category, arrow
from categories.data.tuple import swap
from categories.type import Lambda, hkt, typeclass

__all__ = (
    'Arrow',
)


a = TypeVar('a')

b = TypeVar('b')

b_ = TypeVar('b_')

c = TypeVar('c')

c_ = TypeVar('c_')

d = TypeVar('d')


class Arrow(Category[a], typeclass[a]):
    def arr(self, f : Lambda[b, c], /) -> hkt[a, b, c]: ...

    def first(self, f : hkt[a, b, c], /) -> hkt[a, tuple[b, d], tuple[c, d]]:
        return self.product(f, self.id())

    def second(self, g : hkt[a, b, c], /) -> hkt[a, tuple[d, b], tuple[d, c]]:
        return self.product(self.id(), g)

    def product(self, f : hkt[a, b, c], g : hkt[a, b_, c_], /) -> hkt[a, tuple[b, b_], tuple[c, c_]]:
        return arrow(self, self.first(f), arrow(self, self.arr(swap), arrow(self, self.second(g), self.arr(swap))))

    def fanout(self, f : hkt[a, b, c], g : hkt[a, b, c_], /) -> hkt[a, b, tuple[c, c_]]:
        return arrow(self, self.arr(lambda b, /: (b, b)), self.product(f, g))