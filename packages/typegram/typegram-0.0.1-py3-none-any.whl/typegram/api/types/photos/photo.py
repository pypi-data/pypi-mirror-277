
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



class Photo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.photos.Photo`.

    Details:
        - Layer: ``181``
        - ID: ``20212CA8``

photo (:obj:`Photo<typegram.api.ayiin.Photo>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 12 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            photos.Photo
            photos.Photos
    """

    __slots__: List[str] = ["photo", "users"]

    ID = 0x20212ca8
    QUALNAME = "functions.typesphotos.Photo"

    def __init__(self, *, photo: "ayiin.Photo", users: List["ayiin.User"]) -> None:
        
                self.photo = photo  # Photo
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Photo":
        # No flags
        
        photo = Object.read(b)
        
        users = Object.read(b)
        
        return Photo(photo=photo, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.photo.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()