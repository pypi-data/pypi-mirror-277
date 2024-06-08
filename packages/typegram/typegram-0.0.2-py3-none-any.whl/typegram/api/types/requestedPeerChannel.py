
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



class RequestedPeerChannel(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RequestedPeer`.

    Details:
        - Layer: ``181``
        - ID: ``8BA403E4``

channel_id (``int`` ``64-bit``):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        username (``str``, *optional*):
                    N/A
                
        photo (:obj:`Photo<typegram.api.ayiin.Photo>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["channel_id", "title", "username", "photo"]

    ID = 0x8ba403e4
    QUALNAME = "types.requestedPeerChannel"

    def __init__(self, *, channel_id: int, title: Optional[str] = None, username: Optional[str] = None, photo: "api.ayiin.Photo" = None) -> None:
        
                self.channel_id = channel_id  # long
        
                self.title = title  # string
        
                self.username = username  # string
        
                self.photo = photo  # Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestedPeerChannel":
        
        flags = Int.read(b)
        
        channel_id = Long.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        username = String.read(b) if flags & (1 << 1) else None
        photo = Object.read(b) if flags & (1 << 2) else None
        
        return RequestedPeerChannel(channel_id=channel_id, title=title, username=username, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.username is not None:
            b.write(String(self.username))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()