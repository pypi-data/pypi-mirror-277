
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


MessageEntity = Union[api.types.MessageEntityUnknown, api.types.MessageEntityMention, api.types.MessageEntityHashtag, api.types.MessageEntityBotCommand, api.types.MessageEntityUrl, api.types.MessageEntityEmail, api.types.MessageEntityBold, api.types.MessageEntityItalic, api.types.MessageEntityCode, api.types.MessageEntityPre, api.types.MessageEntityTextUrl, api.types.MessageEntityMentionName, api.types.InputMessageEntityMentionName, api.types.MessageEntityPhone, api.types.MessageEntityCashtag, api.types.MessageEntityUnderline, api.types.MessageEntityStrike, api.types.MessageEntityBankCard, api.types.MessageEntitySpoiler, api.types.MessageEntityCustomEmoji, api.types.MessageEntityBlockquote]


class MessageEntity(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 21 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            messageEntityUnknown
            messageEntityMention
            messageEntityHashtag
            messageEntityBotCommand
            messageEntityUrl
            messageEntityEmail
            messageEntityBold
            messageEntityItalic
            messageEntityCode
            messageEntityPre
            messageEntityTextUrl
            messageEntityMentionName
            inputMessageEntityMentionName
            messageEntityPhone
            messageEntityCashtag
            messageEntityUnderline
            messageEntityStrike
            messageEntityBankCard
            messageEntitySpoiler
            messageEntityCustomEmoji
            messageEntityBlockquote
    """

    QUALNAME = "typegram.api.ayiin.MessageEntity.MessageEntity"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/MessageEntity")