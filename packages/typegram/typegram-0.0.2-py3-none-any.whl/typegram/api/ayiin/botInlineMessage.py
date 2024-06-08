
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


BotInlineMessage = Union[api.types.BotInlineMessageMediaAuto, api.types.BotInlineMessageText, api.types.BotInlineMessageMediaGeo, api.types.BotInlineMessageMediaVenue, api.types.BotInlineMessageMediaContact, api.types.BotInlineMessageMediaInvoice, api.types.BotInlineMessageMediaWebPage]


class BotInlineMessage(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            botInlineMessageMediaAuto
            botInlineMessageText
            botInlineMessageMediaGeo
            botInlineMessageMediaVenue
            botInlineMessageMediaContact
            botInlineMessageMediaInvoice
            botInlineMessageMediaWebPage
    """

    QUALNAME = "typegram.api.ayiin.BotInlineMessage.BotInlineMessage"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/BotInlineMessage")