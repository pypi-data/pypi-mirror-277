from __future__ import annotations

__all__ = ("Menu",)

import asyncio
from itertools import count
from typing import TYPE_CHECKING
from typing import cast
from typing import final

from yatbaf.di import Provide
from yatbaf.handler import Handler
from yatbaf.types import InlineKeyboardMarkup

from .button import Back
from .row import AbstractRowBuilder
from .row import Row

if TYPE_CHECKING:
    from collections.abc import Awaitable
    from collections.abc import Callable
    from collections.abc import Sequence

    from yatbaf.enums import ParseMode
    from yatbaf.group import OnCallbackQuery
    from yatbaf.types import CallbackQuery

    from .button import AbstractButton
    from .typing import Query

_menu_count = count(1).__next__


def _parse_markup(
    markup: list[AbstractButton | AbstractRowBuilder | list[AbstractButton]]
) -> list[AbstractRowBuilder]:
    result: list[AbstractRowBuilder] = []
    for row in markup:
        if isinstance(row, list):
            for obj in row:
                if issubclass(type(obj), AbstractRowBuilder):
                    if len(row) != 1:
                        raise ValueError(
                            f"It is not possible to use {obj!r} with "
                            "other objects in the same row"
                        )
                    result.append(cast("AbstractRowBuilder", obj))
                    break
            else:
                result.append(Row(row))

        # row builder
        elif issubclass(type(row), AbstractRowBuilder):
            result.append(cast("AbstractRowBuilder", row))

        # single button
        else:
            result.append(Row([cast("AbstractButton", row)]))

    return result


def _parse_menu_name(name: str | None) -> str:
    if name is not None:
        return name.lower()
    return f"menu{_menu_count()}"


@final
class Menu:
    """Menu object."""

    __slots__ = (
        "_title",
        "_name",
        "_buttons",
        "_submenu",
        "_rows",
        "_parent",
        "_prefix",
        "_group",
        "_handler",
        "_parse_mode",
    )

    def __init__(  # yapf: disable
        self,
        *,
        title: str | Callable[[Query], Awaitable[str]],
        name: str | None = None,
        buttons: list[AbstractButton | AbstractRowBuilder | list[AbstractButton]] | None = None,  # noqa: E501
        submenu: Sequence[Menu] | None = None,
        group: OnCallbackQuery | None = None,
        back_btn_title: str | Callable | None = None,
        parse_mode: ParseMode | None = None,
    ) -> None:
        """
        :param title: String or Callable which return menu title.
        :param name: *Optional.* Menu name.
        :param submenu: *Optional.* Sequence of :class:`Menu`.
        :param buttons: *Optional.* A list of buttons.
        :param group: *Optional.* Pre-configured handler group.
        :param back_btn_title: *Optional.* Pass a title if you want to add
            a 'back button' to this menu. For submenu only.
        :param parse_mode: *Optional.* Parse mode for menu title.
        """  # noqa: E501
        self._name = _parse_menu_name(name)
        self._title = title
        self._prefix: str | None = None

        buttons = buttons if buttons is not None else []
        if back_btn_title is not None:
            buttons.append(Back(title=back_btn_title))
        if not buttons:
            raise ValueError(f"{self!r} must have at least one button.")

        self._rows = _parse_markup(buttons)

        self._submenu = {} if submenu is None else {m.name: m for m in submenu}
        self._parent: Menu | None = None

        self._group = group
        self._handler = Handler(  # yapf: disable
            fn=self._render,
            update_type="callback_query",
            dependencies={
                "_title": Provide(title if callable(title) else self._get_title),  # noqa: E501
                "_markup": Provide(self._get_markup),
            }
        )
        self._parse_mode = parse_mode

    def __repr__(self) -> str:
        return f"<Menu[{self._name}]>"

    @property
    def name(self) -> str:
        """Menu name."""
        return self._name

    async def provide(self) -> Menu:
        return self

    def get_submenu(self, name: str) -> Menu:
        """Returns submenu by name.

        :param name: Submenu name.
        :raises ValueError: If submenu with ``name`` is not found.
        """
        try:
            return self._submenu[name]
        except KeyError:
            raise ValueError(f"Menu {name} not found in {self!r}") from None

    def get_root(self) -> Menu:
        """Returns main menu."""
        menu = self
        while menu._parent is not None:
            menu = menu._parent
        return menu

    def get_menu(self, path: str) -> Menu:
        """Returns menu by path.

        :param path: Path to menu.
        :raises ValueError: If ``path`` is not found.
        """
        menu = self.get_root()
        for name in path.split("."):
            menu = menu.get_submenu(name)
        return menu

    async def _get_title(self) -> str:
        """Menu title provider. Static title."""
        return self._title  # type: ignore[return-value]

    async def _get_markup(self, update: Query) -> InlineKeyboardMarkup:
        """Menu buttons provider."""
        if len(self._rows) == 1:
            return InlineKeyboardMarkup([
                row for row in await self._rows[0]._build(update)
            ])

        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(r._build(update)) for r in self._rows]
        return InlineKeyboardMarkup([
            row for task in tasks for row in task.result()
        ])

    async def _render(
        self,
        q: Query,
        _title: str,
        _markup: InlineKeyboardMarkup,
    ) -> None:
        """Menu handler callback.

        :param q: Update instance.
        :param _title: Menu title.
        :param _markup: Menu buttons.
        """
        # callback query
        if hasattr(q, "message"):
            if not q.__usrctx__.get("_noanswer", False):
                await q.answer()  # type: ignore[call-arg]
            # q.message is always a Message (filter.HasMessage)
            await q.message.edit(  # type: ignore[union-attr]
                text=_title,
                reply_markup=_markup,
                parse_mode=self._parse_mode,
            )

        # message
        else:
            await q.answer(
                text=_title,
                reply_markup=_markup,
                parse_mode=self._parse_mode,
            )

    async def render(self, q: Query, /) -> None:
        """Render menu."""
        await self._handler._exec(q)

    @staticmethod
    def noanswer(q: CallbackQuery, /) -> None:
        """Use this method before calling :meth:`render` to avoid calling
        `q.answer()` twice, if you use `q.answer()` manually.

        .. note::

            All methods of :class:`~yatbaf_menu.nav.MenuNav` use :meth:`render`.

        :param q: Callback event.
        """
        q.__usrctx__["_noanswer"] = True
