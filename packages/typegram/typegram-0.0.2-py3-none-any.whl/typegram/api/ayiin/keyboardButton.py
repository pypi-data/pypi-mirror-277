
#===========================================================
#            Copyright (C) 2023-present AyiinXd
#===========================================================
#||                                                       ||
#||              _         _ _      __  __   _            ||
#||             /   _   _(_|_)_ __  / /__| |           ||
#||            / _ | | | | | | '_     _  | |           ||
#||           / ___  |_| | | | | | |/   (_| |           ||
#||          /_/   ___, |_|_|_| |_/_/___,_|           ||
#||                  |___/                                ||
#||                                                       ||
#===========================================================
# Appreciating the work of others is not detrimental to you
#===========================================================
#

from typing import Union, List, Optional

from typegram import api
from typegram.api.object import Object


KeyboardButton = Union[api.types.KeyboardButton, api.types.KeyboardButtonUrl, api.types.KeyboardButtonCallback, api.types.KeyboardButtonRequestPhone, api.types.KeyboardButtonRequestGeoLocation, api.types.KeyboardButtonSwitchInline, api.types.KeyboardButtonGame, api.types.KeyboardButtonBuy, api.types.KeyboardButtonUrlAuth, api.types.InputKeyboardButtonUrlAuth, api.types.KeyboardButtonRequestPoll, api.types.InputKeyboardButtonUserProfile, api.types.KeyboardButtonUserProfile, api.types.KeyboardButtonWebView, api.types.KeyboardButtonSimpleWebView, api.types.KeyboardButtonRequestPeer, api.types.InputKeyboardButtonRequestPeer]


class KeyboardButton(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 17 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            keyboardButton
            keyboardButtonUrl
            keyboardButtonCallback
            keyboardButtonRequestPhone
            keyboardButtonRequestGeoLocation
            keyboardButtonSwitchInline
            keyboardButtonGame
            keyboardButtonBuy
            keyboardButtonUrlAuth
            inputKeyboardButtonUrlAuth
            keyboardButtonRequestPoll
            inputKeyboardButtonUserProfile
            keyboardButtonUserProfile
            keyboardButtonWebView
            keyboardButtonSimpleWebView
            keyboardButtonRequestPeer
            inputKeyboardButtonRequestPeer
    """

    QUALNAME = "typegram.api.ayiin.KeyboardButton.KeyboardButton"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/KeyboardButton")