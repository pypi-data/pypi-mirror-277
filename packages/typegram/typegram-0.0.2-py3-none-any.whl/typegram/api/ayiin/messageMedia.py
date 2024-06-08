
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


MessageMedia = Union[api.types.MessageMediaPhoto, api.types.MessageMediaGeo, api.types.MessageMediaContact, api.types.MessageMediaDocument, api.types.MessageMediaWebPage, api.types.MessageMediaVenue, api.types.MessageMediaGame, api.types.MessageMediaInvoice, api.types.MessageMediaGeoLive, api.types.MessageMediaPoll, api.types.MessageMediaDice, api.types.MessageMediaStory, api.types.MessageMediaGiveaway, api.types.MessageMediaGiveawayResults]


class MessageMedia(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 14 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            messageMediaPhoto
            messageMediaGeo
            messageMediaContact
            messageMediaDocument
            messageMediaWebPage
            messageMediaVenue
            messageMediaGame
            messageMediaInvoice
            messageMediaGeoLive
            messageMediaPoll
            messageMediaDice
            messageMediaStory
            messageMediaGiveaway
            messageMediaGiveawayResults
    """

    QUALNAME = "typegram.api.ayiin.MessageMedia.MessageMedia"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/MessageMedia")