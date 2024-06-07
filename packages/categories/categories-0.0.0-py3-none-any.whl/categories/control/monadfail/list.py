from __future__ import annotations

from typing import TypeVar

from categories.control.monad import MonadList

from . import MonadFail

__all__ = (
    'MonadFailList',
)


a = TypeVar('a')


class MonadFailList(MonadList, MonadFail[list]):
    def fail(self, _ : str, /) -> list[a]:
        return []