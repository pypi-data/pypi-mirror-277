from __future__ import annotations

from typing import TypeVar

from categories.control.applicative import ApplicativeList

from . import Alternative

__all__ = (
    'AlternativeList',
)


a = TypeVar('a')

b = TypeVar('b')


class AlternativeList(ApplicativeList, Alternative[list]):
    def empty(self, /) -> list[a]:
        return []

    def alt(self, xs : list[a], ys : list[a], /) -> list[a]:
        return xs + ys