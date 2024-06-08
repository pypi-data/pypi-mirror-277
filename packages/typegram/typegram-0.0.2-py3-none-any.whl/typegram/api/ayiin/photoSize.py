
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


PhotoSize = Union[api.types.PhotoSizeEmpty, api.types.PhotoSize, api.types.PhotoCachedSize, api.types.PhotoStrippedSize, api.types.PhotoSizeProgressive, api.types.PhotoPathSize]


class PhotoSize(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            photoSizeEmpty
            photoSize
            photoCachedSize
            photoStrippedSize
            photoSizeProgressive
            photoPathSize
    """

    QUALNAME = "typegram.api.ayiin.PhotoSize.PhotoSize"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/PhotoSize")