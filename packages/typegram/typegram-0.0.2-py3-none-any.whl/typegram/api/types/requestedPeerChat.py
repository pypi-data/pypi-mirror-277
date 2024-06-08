
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



class RequestedPeerChat(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RequestedPeer`.

    Details:
        - Layer: ``181``
        - ID: ``7307544F``

chat_id (``int`` ``64-bit``):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        photo (:obj:`Photo<typegram.api.ayiin.Photo>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["chat_id", "title", "photo"]

    ID = 0x7307544f
    QUALNAME = "types.requestedPeerChat"

    def __init__(self, *, chat_id: int, title: Optional[str] = None, photo: "api.ayiin.Photo" = None) -> None:
        
                self.chat_id = chat_id  # long
        
                self.title = title  # string
        
                self.photo = photo  # Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestedPeerChat":
        
        flags = Int.read(b)
        
        chat_id = Long.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        photo = Object.read(b) if flags & (1 << 2) else None
        
        return RequestedPeerChat(chat_id=chat_id, title=title, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.chat_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()