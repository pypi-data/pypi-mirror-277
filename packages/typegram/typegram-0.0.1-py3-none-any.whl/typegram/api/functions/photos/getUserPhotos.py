
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



class GetUserPhotos(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``91CD32A8``

user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        offset (``int`` ``32-bit``):
                    N/A
                
        max_id (``int`` ``64-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`photos.Photos<typegram.api.ayiin.photos.Photos>`
    """

    __slots__: List[str] = ["user_id", "offset", "max_id", "limit"]

    ID = 0x91cd32a8
    QUALNAME = "functions.functionsphotos.Photos"

    def __init__(self, *, user_id: "ayiin.InputUser", offset: int, max_id: int, limit: int) -> None:
        
                self.user_id = user_id  # InputUser
        
                self.offset = offset  # int
        
                self.max_id = max_id  # long
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUserPhotos":
        # No flags
        
        user_id = Object.read(b)
        
        offset = Int.read(b)
        
        max_id = Long.read(b)
        
        limit = Int.read(b)
        
        return GetUserPhotos(user_id=user_id, offset=offset, max_id=max_id, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(Int(self.offset))
        
        b.write(Long(self.max_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()