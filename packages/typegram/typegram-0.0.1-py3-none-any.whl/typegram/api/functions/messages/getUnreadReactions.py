
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



class GetUnreadReactions(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3223495B``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        offset_id (``int`` ``32-bit``):
                    N/A
                
        add_offset (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        max_id (``int`` ``32-bit``):
                    N/A
                
        min_id (``int`` ``32-bit``):
                    N/A
                
        top_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.Messages<typegram.api.ayiin.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "offset_id", "add_offset", "limit", "max_id", "min_id", "top_msg_id"]

    ID = 0x3223495b
    QUALNAME = "functions.functionsmessages.Messages"

    def __init__(self, *, peer: "ayiin.InputPeer", offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.offset_id = offset_id  # int
        
                self.add_offset = add_offset  # int
        
                self.limit = limit  # int
        
                self.max_id = max_id  # int
        
                self.min_id = min_id  # int
        
                self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUnreadReactions":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        offset_id = Int.read(b)
        
        add_offset = Int.read(b)
        
        limit = Int.read(b)
        
        max_id = Int.read(b)
        
        min_id = Int.read(b)
        
        return GetUnreadReactions(peer=peer, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.add_offset))
        
        b.write(Int(self.limit))
        
        b.write(Int(self.max_id))
        
        b.write(Int(self.min_id))
        
        return b.getvalue()