import sys
import unittest.mock as mock

import pytest

from yatbaf.enums import UpdateType
from yatbaf.group import OnBusinessConnection
from yatbaf.group import OnBusinessMessage
from yatbaf.group import OnCallbackQuery
from yatbaf.group import OnChannelPost
from yatbaf.group import OnChatBoost
from yatbaf.group import OnChatJoinRequest
from yatbaf.group import OnChatMember
from yatbaf.group import OnChosenInlineResult
from yatbaf.group import OnDeletedBusinessMessages
from yatbaf.group import OnEditedBusinessMessage
from yatbaf.group import OnEditedChannelPost
from yatbaf.group import OnEditedMessage
from yatbaf.group import OnInlineQuery
from yatbaf.group import OnMessage
from yatbaf.group import OnMessageReaction
from yatbaf.group import OnMessageReactionCount
from yatbaf.group import OnMyChatMember
from yatbaf.group import OnPoll
from yatbaf.group import OnPollAnswer
from yatbaf.group import OnPreCheckoutQuery
from yatbaf.group import OnRemovedChatBoost
from yatbaf.group import OnShippingQuery
from yatbaf.handler import Handler
from yatbaf.middleware import Middleware

MODULE = sys.modules["yatbaf.group"]


def test_update_type():
    # yapf: disable
    assert OnCallbackQuery().update_type == UpdateType.CALLBACK_QUERY
    assert OnChannelPost().update_type == UpdateType.CHANNEL_POST
    assert OnChatJoinRequest().update_type == UpdateType.CHAT_JOIN_REQUEST
    assert OnChatMember().update_type == UpdateType.CHAT_MEMBER
    assert OnChosenInlineResult().update_type == UpdateType.CHOSEN_INLINE_RESULT
    assert OnEditedChannelPost().update_type == UpdateType.EDITED_CHANNEL_POST
    assert OnEditedMessage().update_type == UpdateType.EDITED_MESSAGE
    assert OnInlineQuery().update_type == UpdateType.INLINE_QUERY
    assert OnMessage().update_type == UpdateType.MESSAGE
    assert OnMyChatMember().update_type == UpdateType.MY_CHAT_MEMBER
    assert OnPoll().update_type == UpdateType.POLL
    assert OnPollAnswer().update_type == UpdateType.POLL_ANSWER
    assert OnPreCheckoutQuery().update_type == UpdateType.PRE_CHECKOUT_QUERY
    assert OnShippingQuery().update_type == UpdateType.SHIPPING_QUERY
    assert OnChatBoost().update_type == UpdateType.CHAT_BOOST
    assert OnRemovedChatBoost().update_type == UpdateType.REMOVED_CHAT_BOOST
    assert OnMessageReaction().update_type == UpdateType.MESSAGE_REACTION
    assert OnMessageReactionCount().update_type == UpdateType.MESSAGE_REACTION_COUNT  # noqa: E501
    assert OnBusinessConnection().update_type == UpdateType.BUSINESS_CONNECTION
    assert OnBusinessMessage().update_type == UpdateType.BUSINESS_MESSAGE
    assert OnEditedBusinessMessage().update_type == UpdateType.EDITED_BUSINESS_MESSAGE  # noqa: 501
    assert OnDeletedBusinessMessages().update_type == UpdateType.DELETED_BUSINESS_MESSAGES  # noqa: 501
    # yapf: enable


def test_new_router():
    router = OnMessage()
    assert not router._frozen
    assert not router._handlers
    assert not router._handler_guards
    assert not router._handler_middleware
    assert not router._guards
    assert not router._middleware
    assert not router._filters
    assert not router._stop_propagate


def test_on_registration(monkeypatch):
    monkeypatch.setattr(MODULE, "wrap_middleware", wm := mock.Mock())
    monkeypatch.setattr(OnMessage, "_resolve_guards", rg := mock.Mock())
    monkeypatch.setattr(OnMessage, "_resolve_middleware", rmw := mock.Mock())
    monkeypatch.setattr(OnMessage, "_prepare_handlers", ph := mock.Mock())
    router = OnMessage()
    router.on_registration()

    assert router._frozen
    rmw.assert_called_once()
    ph.assert_called_once()
    rg.assert_called_once()
    wm.assert_called_once_with(router._handle, router._middleware)


async def fn(_):
    pass


def _handler(fn):
    return Handler("message", fn=fn)


async def guard(_):
    pass


def middleware(h):

    async def w(u):
        await h(u)

    return w


@pytest.mark.parametrize(
    "objs",
    [
        (
            OnMessage(),
            OnMessage(),
        ),
        (
            OnMessage(handler_guards=[guard]),
            OnMessage(handler_guards=[guard]),
        ),
        (
            OnMessage(handlers=[_handler(fn)]),
            OnMessage(handlers=[_handler(fn)]),
        ),
        (
            OnMessage(handler_guards=[guard], handlers=[_handler(fn)]),
            OnMessage(handler_guards=[guard], handlers=[_handler(fn)]),
        ),
        (
            OnMessage(
                handler_middleware=[middleware],
                handler_guards=[guard],
                handlers=[_handler(fn)]
            ),
            OnMessage(
                handler_middleware=[middleware],
                handler_guards=[guard],
                handlers=[_handler(fn)],
            ),
        ),
        (
            OnMessage(
                handler_middleware=[Middleware(middleware)],
                handler_guards=[guard],
                handlers=[_handler(fn)]
            ),
            OnMessage(
                handler_middleware=[Middleware(middleware)],
                handler_guards=[guard],
                handlers=[_handler(fn)],
            ),
        ),
    ]
)
def test_eq(objs):
    router1, router2 = objs
    assert router1 == router2


@pytest.mark.parametrize("r1", [OnMessage()])
@pytest.mark.parametrize(
    "r2",
    [
        OnMessage(handlers=[_handler(fn)]),
        OnMessage(handler_middleware=[middleware]),
        OnMessage(handler_guards=[guard]),
        OnMessage(
            handlers=[_handler(fn)],
            handler_middleware=[middleware],
        ),
        OnMessage(
            handlers=[_handler(fn)],
            handler_middleware=[middleware],
            handler_guards=[middleware],
        ),
        OnPoll(),
        OnCallbackQuery(),
    ]
)
def test_not_eq(r1, r2):
    assert r1 != r2
