
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


InputMedia = Union[api.types.InputMediaUploadedPhoto, api.types.InputMediaPhoto, api.types.InputMediaGeoPoint, api.types.InputMediaContact, api.types.InputMediaUploadedDocument, api.types.InputMediaDocument, api.types.InputMediaVenue, api.types.InputMediaPhotoExternal, api.types.InputMediaDocumentExternal, api.types.InputMediaGame, api.types.InputMediaInvoice, api.types.InputMediaGeoLive, api.types.InputMediaPoll, api.types.InputMediaDice, api.types.InputMediaStory, api.types.InputMediaWebPage]


class InputMedia(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 16 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            inputMediaUploadedPhoto
            inputMediaPhoto
            inputMediaGeoPoint
            inputMediaContact
            inputMediaUploadedDocument
            inputMediaDocument
            inputMediaVenue
            inputMediaPhotoExternal
            inputMediaDocumentExternal
            inputMediaGame
            inputMediaInvoice
            inputMediaGeoLive
            inputMediaPoll
            inputMediaDice
            inputMediaStory
            inputMediaWebPage
    """

    QUALNAME = "typegram.api.ayiin.InputMedia.InputMedia"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/InputMedia")