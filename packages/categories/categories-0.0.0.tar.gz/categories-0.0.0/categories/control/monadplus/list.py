from __future__ import annotations

from categories.control.alternative import AlternativeList
from categories.control.monad import MonadList

from . import MonadPlus

__all__ = (
    'MonadPlusList',
)


class MonadPlusList(AlternativeList, MonadList, MonadPlus[list]): ...