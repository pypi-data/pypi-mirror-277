
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



class GetSearchCounters(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``1BBCF300``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        filters (List of :obj:`MessagesFilter<typegram.api.ayiin.MessagesFilter>`):
                    N/A
                
        saved_peer_id (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
        top_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        List of :obj:`messages.SearchCounter<typegram.api.ayiin.messages.SearchCounter>`
    """

    __slots__: List[str] = ["peer", "filters", "saved_peer_id", "top_msg_id"]

    ID = 0x1bbcf300
    QUALNAME = "functions.functionsVector<messages.SearchCounter>"

    def __init__(self, *, peer: "ayiin.InputPeer", filters: List["ayiin.MessagesFilter"], saved_peer_id: "ayiin.InputPeer" = None, top_msg_id: Optional[int] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.filters = filters  # MessagesFilter
        
                self.saved_peer_id = saved_peer_id  # InputPeer
        
                self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSearchCounters":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        saved_peer_id = Object.read(b) if flags & (1 << 2) else None
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        filters = Object.read(b)
        
        return GetSearchCounters(peer=peer, filters=filters, saved_peer_id=saved_peer_id, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(Vector(self.filters))
        
        return b.getvalue()