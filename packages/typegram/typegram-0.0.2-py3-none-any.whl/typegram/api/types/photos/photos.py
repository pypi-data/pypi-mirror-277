
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

from io import BytesIO
from typing import Any, Union, List, Optional

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class Photos(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.photos.Photos`.

    Details:
        - Layer: ``181``
        - ID: ``8DCA6AA5``

photos (List of :obj:`Photo<typegram.api.ayiin.Photo>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 13 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            photos.getUserPhotos
    """

    __slots__: List[str] = ["photos", "users"]

    ID = 0x8dca6aa5
    QUALNAME = "types.photos.photos"

    def __init__(self, *, photos: List["api.ayiin.Photo"], users: List["api.ayiin.User"]) -> None:
        
                self.photos = photos  # Photo
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Photos":
        # No flags
        
        photos = Object.read(b)
        
        users = Object.read(b)
        
        return Photos(photos=photos, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.photos))
        
        b.write(Vector(self.users))
        
        return b.getvalue()