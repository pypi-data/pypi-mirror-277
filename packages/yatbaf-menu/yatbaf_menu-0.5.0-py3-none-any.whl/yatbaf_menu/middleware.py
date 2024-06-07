from __future__ import annotations

from typing import TYPE_CHECKING

from .nav import MenuNav

if TYPE_CHECKING:
    from yatbaf.types import CallbackQuery
    from yatbaf.typing import HandlerCallableType

    from .menu import Menu


class CutPayloadMiddileware:
    __slots__ = ("_fn",)

    def __init__(self, fn: HandlerCallableType[CallbackQuery]) -> None:
        self._fn = fn

    async def __call__(self, q: CallbackQuery) -> None:
        # root menu (2ch) + version (2ch) + menu (2ch) + button (2ch)
        q.data = q.data[8:]  # type: ignore[index]
        await self._fn(q)


class InjectMenuMiddleware:
    __slots__ = (
        "_fn",
        "_menu",
    )

    def __init__(
        self, fn: HandlerCallableType[CallbackQuery], menu: Menu
    ) -> None:
        self._fn = fn
        self._menu = menu

    async def __call__(self, q: CallbackQuery) -> None:
        q.ctx["nav"] = MenuNav(self._menu, q)
        await self._fn(q)
