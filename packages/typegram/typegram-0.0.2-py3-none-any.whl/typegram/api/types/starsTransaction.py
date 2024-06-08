
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



class StarsTransaction(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StarsTransaction`.

    Details:
        - Layer: ``181``
        - ID: ``CC7079B2``

id (``str``):
                    N/A
                
        stars (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        peer (:obj:`StarsTransactionPeer<typegram.api.ayiin.StarsTransactionPeer>`):
                    N/A
                
        refund (``bool``, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        description (``str``, *optional*):
                    N/A
                
        photo (:obj:`WebDocument<typegram.api.ayiin.WebDocument>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "stars", "date", "peer", "refund", "title", "description", "photo"]

    ID = 0xcc7079b2
    QUALNAME = "types.starsTransaction"

    def __init__(self, *, id: str, stars: int, date: int, peer: "api.ayiin.StarsTransactionPeer", refund: Optional[bool] = None, title: Optional[str] = None, description: Optional[str] = None, photo: "api.ayiin.WebDocument" = None) -> None:
        
                self.id = id  # string
        
                self.stars = stars  # long
        
                self.date = date  # int
        
                self.peer = peer  # StarsTransactionPeer
        
                self.refund = refund  # true
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.photo = photo  # WebDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsTransaction":
        
        flags = Int.read(b)
        
        refund = True if flags & (1 << 3) else False
        id = String.read(b)
        
        stars = Long.read(b)
        
        date = Int.read(b)
        
        peer = Object.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        photo = Object.read(b) if flags & (1 << 2) else None
        
        return StarsTransaction(id=id, stars=stars, date=date, peer=peer, refund=refund, title=title, description=description, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        b.write(Long(self.stars))
        
        b.write(Int(self.date))
        
        b.write(self.peer.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()