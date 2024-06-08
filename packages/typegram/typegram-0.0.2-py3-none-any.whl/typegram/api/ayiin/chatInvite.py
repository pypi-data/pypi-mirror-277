
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


ChatInvite = Union[api.types.ChatInviteAlready, api.types.ChatInvite, api.types.ChatInvitePeek]


class ChatInvite(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            chatInviteAlready
            chatInvite
            chatInvitePeek
    """

    QUALNAME = "typegram.api.ayiin.ChatInvite.ChatInvite"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/ChatInvite")