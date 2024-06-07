
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



class GetStoryPublicForwards(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A6437EF6``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        offset (``str``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`stats.PublicForwards<typegram.api.ayiin.stats.PublicForwards>`
    """

    __slots__: List[str] = ["peer", "id", "offset", "limit"]

    ID = 0xa6437ef6
    QUALNAME = "functions.functionsstats.PublicForwards"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int, offset: str, limit: int) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.offset = offset  # string
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryPublicForwards":
        # No flags
        
        peer = Object.read(b)
        
        id = Int.read(b)
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        return GetStoryPublicForwards(peer=peer, id=id, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()