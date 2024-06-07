
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

from typegram.api import ayiin, functions
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class PhotosSlice(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.photos.Photos`.

    Details:
        - Layer: ``181``
        - ID: ``15051F54``

count (``int`` ``32-bit``):
                    N/A
                
        photos (List of :obj:`Photo<typegram.api.ayiin.Photo>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 13 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            photos.Photo
            photos.Photos
    """

    __slots__: List[str] = ["count", "photos", "users"]

    ID = 0x15051f54
    QUALNAME = "functions.typesphotos.Photos"

    def __init__(self, *, count: int, photos: List["ayiin.Photo"], users: List["ayiin.User"]) -> None:
        
                self.count = count  # int
        
                self.photos = photos  # Photo
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotosSlice":
        # No flags
        
        count = Int.read(b)
        
        photos = Object.read(b)
        
        users = Object.read(b)
        
        return PhotosSlice(count=count, photos=photos, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.photos))
        
        b.write(Vector(self.users))
        
        return b.getvalue()