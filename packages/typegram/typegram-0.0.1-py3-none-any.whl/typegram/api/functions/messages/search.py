
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



class Search(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``29EE847A``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        q (``str``):
                    N/A
                
        filter (:obj:`MessagesFilter<typegram.api.ayiin.MessagesFilter>`):
                    N/A
                
        min_date (``int`` ``32-bit``):
                    N/A
                
        max_date (``int`` ``32-bit``):
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
                
        hash (``int`` ``64-bit``):
                    N/A
                
        from_id (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
        saved_peer_id (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
        saved_reaction (List of :obj:`Reaction<typegram.api.ayiin.Reaction>`, *optional*):
                    N/A
                
        top_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.Messages<typegram.api.ayiin.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "q", "filter", "min_date", "max_date", "offset_id", "add_offset", "limit", "max_id", "min_id", "hash", "from_id", "saved_peer_id", "saved_reaction", "top_msg_id"]

    ID = 0x29ee847a
    QUALNAME = "functions.functionsmessages.Messages"

    def __init__(self, *, peer: "ayiin.InputPeer", q: str, filter: "ayiin.MessagesFilter", min_date: int, max_date: int, offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int, from_id: "ayiin.InputPeer" = None, saved_peer_id: "ayiin.InputPeer" = None, saved_reaction: Optional[List["ayiin.Reaction"]] = None, top_msg_id: Optional[int] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.q = q  # string
        
                self.filter = filter  # MessagesFilter
        
                self.min_date = min_date  # int
        
                self.max_date = max_date  # int
        
                self.offset_id = offset_id  # int
        
                self.add_offset = add_offset  # int
        
                self.limit = limit  # int
        
                self.max_id = max_id  # int
        
                self.min_id = min_id  # int
        
                self.hash = hash  # long
        
                self.from_id = from_id  # InputPeer
        
                self.saved_peer_id = saved_peer_id  # InputPeer
        
                self.saved_reaction = saved_reaction  # Reaction
        
                self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Search":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        q = String.read(b)
        
        from_id = Object.read(b) if flags & (1 << 0) else None
        
        saved_peer_id = Object.read(b) if flags & (1 << 2) else None
        
        saved_reaction = Object.read(b) if flags & (1 << 3) else []
        
        top_msg_id = Int.read(b) if flags & (1 << 1) else None
        filter = Object.read(b)
        
        min_date = Int.read(b)
        
        max_date = Int.read(b)
        
        offset_id = Int.read(b)
        
        add_offset = Int.read(b)
        
        limit = Int.read(b)
        
        max_id = Int.read(b)
        
        min_id = Int.read(b)
        
        hash = Long.read(b)
        
        return Search(peer=peer, q=q, filter=filter, min_date=min_date, max_date=max_date, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash, from_id=from_id, saved_peer_id=saved_peer_id, saved_reaction=saved_reaction, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.q))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())
        
        if self.saved_reaction is not None:
            b.write(Vector(self.saved_reaction))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(self.filter.write())
        
        b.write(Int(self.min_date))
        
        b.write(Int(self.max_date))
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.add_offset))
        
        b.write(Int(self.limit))
        
        b.write(Int(self.max_id))
        
        b.write(Int(self.min_id))
        
        b.write(Long(self.hash))
        
        return b.getvalue()