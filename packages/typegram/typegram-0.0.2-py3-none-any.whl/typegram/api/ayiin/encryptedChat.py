
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


EncryptedChat = Union[api.types.EncryptedChatEmpty, api.types.EncryptedChatWaiting, api.types.EncryptedChatRequested, api.types.EncryptedChat, api.types.EncryptedChatDiscarded]


class EncryptedChat(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            encryptedChatEmpty
            encryptedChatWaiting
            encryptedChatRequested
            encryptedChat
            encryptedChatDiscarded
    """

    QUALNAME = "typegram.api.ayiin.EncryptedChat.EncryptedChat"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/EncryptedChat")