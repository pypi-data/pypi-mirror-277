from __future__ import annotations

__all__ = ("MenuNav",)

from typing import TYPE_CHECKING
from typing import cast

from yatbaf.exceptions import MethodInvokeError

if TYPE_CHECKING:
    from yatbaf.types import CallbackQuery
    from yatbaf.types import Message

    from .menu import Menu


class MenuNav:
    """Menu navigation.

    Use `update.ctx["nav"]` to access this object inside the button callback::

        async def button_action(q: CallbackQuery) -> None:
            nav = q.ctx["nav"]
            ...
    """

    __slots__ = (
        "_query",
        "_menu",
    )

    def __init__(self, menu: Menu, query: CallbackQuery, /) -> None:
        """
        :param menu: Current menu.
        :param query: Current query.
        """
        self._query = query
        self._menu = menu

    @property
    def menu(self) -> Menu:
        """Current :class:`~yatbaf_menu.menu.Menu` instance."""
        return self._menu

    async def navigate(self, path: str, /) -> None:
        """Use this method to open menu by path.

        :param path: Path relative to main menu. Separated by dots.
        """
        menu = self._menu.get_menu(path)
        await menu.render(self._query)

    async def back(self) -> None:
        """Use this method to go to previous menu."""
        menu = self._menu._parent
        if menu is None:
            return
        await menu.render(self._query)

    async def root(self) -> None:
        """Use this method to go to main menu."""
        menu = self._menu.get_root()
        await menu.render(self._query)

    async def submenu(self, name: str) -> None:
        """Use this method to go to submenu.

        :param name: Submenu name.
        """
        menu = self._menu.get_submenu(name)
        await menu.render(self._query)

    async def refresh(self) -> None:
        """Use this method to refresh current menu."""
        await self._menu.render(self._query)

    async def close(self) -> None:
        """Use this method to close the menu."""
        message = cast("Message", self._query.message)
        try:
            await message.delete()
        except MethodInvokeError:
            await message.edit_reply_markup()
