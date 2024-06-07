
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



class GetSavedDialogs(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``5381D21A``

offset_date (``int`` ``32-bit``):
                    N/A
                
        offset_id (``int`` ``32-bit``):
                    N/A
                
        offset_peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        hash (``int`` ``64-bit``):
                    N/A
                
        exclude_pinned (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.SavedDialogs<typegram.api.ayiin.messages.SavedDialogs>`
    """

    __slots__: List[str] = ["offset_date", "offset_id", "offset_peer", "limit", "hash", "exclude_pinned"]

    ID = 0x5381d21a
    QUALNAME = "functions.functionsmessages.SavedDialogs"

    def __init__(self, *, offset_date: int, offset_id: int, offset_peer: "ayiin.InputPeer", limit: int, hash: int, exclude_pinned: Optional[bool] = None) -> None:
        
                self.offset_date = offset_date  # int
        
                self.offset_id = offset_id  # int
        
                self.offset_peer = offset_peer  # InputPeer
        
                self.limit = limit  # int
        
                self.hash = hash  # long
        
                self.exclude_pinned = exclude_pinned  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedDialogs":
        
        flags = Int.read(b)
        
        exclude_pinned = True if flags & (1 << 0) else False
        offset_date = Int.read(b)
        
        offset_id = Int.read(b)
        
        offset_peer = Object.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetSavedDialogs(offset_date=offset_date, offset_id=offset_id, offset_peer=offset_peer, limit=limit, hash=hash, exclude_pinned=exclude_pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.offset_date))
        
        b.write(Int(self.offset_id))
        
        b.write(self.offset_peer.write())
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()