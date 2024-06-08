
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



class RequestedPeerUser(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RequestedPeer`.

    Details:
        - Layer: ``181``
        - ID: ``D62FF46A``

user_id (``int`` ``64-bit``):
                    N/A
                
        first_name (``str``, *optional*):
                    N/A
                
        last_name (``str``, *optional*):
                    N/A
                
        username (``str``, *optional*):
                    N/A
                
        photo (:obj:`Photo<typegram.api.ayiin.Photo>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["user_id", "first_name", "last_name", "username", "photo"]

    ID = 0xd62ff46a
    QUALNAME = "types.requestedPeerUser"

    def __init__(self, *, user_id: int, first_name: Optional[str] = None, last_name: Optional[str] = None, username: Optional[str] = None, photo: "api.ayiin.Photo" = None) -> None:
        
                self.user_id = user_id  # long
        
                self.first_name = first_name  # string
        
                self.last_name = last_name  # string
        
                self.username = username  # string
        
                self.photo = photo  # Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestedPeerUser":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        first_name = String.read(b) if flags & (1 << 0) else None
        last_name = String.read(b) if flags & (1 << 0) else None
        username = String.read(b) if flags & (1 << 1) else None
        photo = Object.read(b) if flags & (1 << 2) else None
        
        return RequestedPeerUser(user_id=user_id, first_name=first_name, last_name=last_name, username=username, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        if self.first_name is not None:
            b.write(String(self.first_name))
        
        if self.last_name is not None:
            b.write(String(self.last_name))
        
        if self.username is not None:
            b.write(String(self.username))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()