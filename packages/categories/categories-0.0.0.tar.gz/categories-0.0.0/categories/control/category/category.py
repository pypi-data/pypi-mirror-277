from __future__ import annotations

from typing import TypeVar

from categories.type import hkt, typeclass

__all__ = (
    'Category',
    'arrow',
)


a = TypeVar('a')

b = TypeVar('b')

c = TypeVar('c')

cat = TypeVar('cat')


class Category(typeclass[cat]):
    def id(self, /) -> hkt[cat, a, a]: ...

    def o(self, f : hkt[cat, b, c], g : hkt[cat, a, b], /) -> hkt[cat, a, c]: ...


def arrow(inst : Category[cat], f : hkt[cat, a, b], g : hkt[cat, b, c], /) -> hkt[cat, a, c]:
    return inst.o(g, f)