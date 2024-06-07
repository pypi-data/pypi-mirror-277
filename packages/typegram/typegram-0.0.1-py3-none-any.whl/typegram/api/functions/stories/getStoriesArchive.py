
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



class GetStoriesArchive(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B4352016``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        offset_id (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`stories.Stories<typegram.api.ayiin.stories.Stories>`
    """

    __slots__: List[str] = ["peer", "offset_id", "limit"]

    ID = 0xb4352016
    QUALNAME = "functions.functionsstories.Stories"

    def __init__(self, *, peer: "ayiin.InputPeer", offset_id: int, limit: int) -> None:
        
                self.peer = peer  # InputPeer
        
                self.offset_id = offset_id  # int
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoriesArchive":
        # No flags
        
        peer = Object.read(b)
        
        offset_id = Int.read(b)
        
        limit = Int.read(b)
        
        return GetStoriesArchive(peer=peer, offset_id=offset_id, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()