import unittest.mock as mock

import pytest

from yatbaf.types import InlineKeyboardMarkup
from yatbaf_menu import URL
from yatbaf_menu import Menu


@pytest.mark.asyncio
async def test_render_message():
    message = mock.AsyncMock(["answer"], answer=mock.AsyncMock())
    menu = Menu(title="menu", buttons=[URL("title", "https://example.com")])
    await menu._render(
        message,
        _title="title",
        _markup=InlineKeyboardMarkup([]),
    )
    message.answer.assert_awaited_once_with(
        text="title",
        reply_markup=InlineKeyboardMarkup([]),
        parse_mode=None,
    )


@pytest.mark.asyncio
async def test_render_callback_query():
    query = mock.AsyncMock(
        ["answer", "message", "__usrctx__"],
        answer=mock.AsyncMock(),
        message=mock.AsyncMock(),
        __usrctx__={},
    )
    menu = Menu(title="menu", buttons=[URL("title", "https://example.com")])
    await menu._render(
        query,
        _title="title",
        _markup=InlineKeyboardMarkup([]),
    )
    query.answer.assert_awaited_once()
    query.message.edit.assert_awaited_once_with(
        text="title",
        reply_markup=InlineKeyboardMarkup([]),
        parse_mode=None,
    )


@pytest.mark.asyncio
async def test_render_callback_query_noanswer():
    query = mock.AsyncMock(
        ["answer", "message", "__usrctx__"],
        answer=mock.AsyncMock(),
        message=mock.AsyncMock(),
        __usrctx__={"_noanswer": True},
    )
    menu = Menu(title="menu", buttons=[URL("title", "https://example.com")])
    await menu._render(
        query,
        _title="title",
        _markup=InlineKeyboardMarkup([]),
    )
    query.answer.assert_not_awaited()
    query.message.edit.assert_awaited_once_with(
        text="title",
        reply_markup=InlineKeyboardMarkup([]),
        parse_mode=None,
    )
