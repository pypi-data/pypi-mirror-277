from __future__ import annotations

from typing import TypeVar

from categories.control.applicative import ApplicativeIO
from categories.type import IO

from . import Alternative

__all__ = (
    'AlternativeIO',
)


a = TypeVar('a')


class AlternativeIO(ApplicativeIO, Alternative[IO]):
    async def empty(self, /) -> a:
        raise Exception('mzero')

    async def alt(self, m : IO[a], m_ : IO[a], /) -> a:
        try:
            return await m
        except BaseException:
            return await m_