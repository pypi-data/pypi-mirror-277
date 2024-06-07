from __future__ import annotations

from typing import TypeVar

from categories.control.monad import Monad
from categories.type import hkt, typeclass

__all__ = (
    'MonadFail',
)


a = TypeVar('a')

m = TypeVar('m')


class MonadFail(Monad[m], typeclass[m]):
    def fail(self, x : str, /) -> hkt[m, a]: ...