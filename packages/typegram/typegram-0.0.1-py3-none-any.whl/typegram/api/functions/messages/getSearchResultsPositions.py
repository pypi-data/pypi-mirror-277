
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



class GetSearchResultsPositions(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9C7F2F10``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        filter (:obj:`MessagesFilter<typegram.api.ayiin.MessagesFilter>`):
                    N/A
                
        offset_id (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        saved_peer_id (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.SearchResultsPositions<typegram.api.ayiin.messages.SearchResultsPositions>`
    """

    __slots__: List[str] = ["peer", "filter", "offset_id", "limit", "saved_peer_id"]

    ID = 0x9c7f2f10
    QUALNAME = "functions.functionsmessages.SearchResultsPositions"

    def __init__(self, *, peer: "ayiin.InputPeer", filter: "ayiin.MessagesFilter", offset_id: int, limit: int, saved_peer_id: "ayiin.InputPeer" = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.filter = filter  # MessagesFilter
        
                self.offset_id = offset_id  # int
        
                self.limit = limit  # int
        
                self.saved_peer_id = saved_peer_id  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSearchResultsPositions":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        saved_peer_id = Object.read(b) if flags & (1 << 2) else None
        
        filter = Object.read(b)
        
        offset_id = Int.read(b)
        
        limit = Int.read(b)
        
        return GetSearchResultsPositions(peer=peer, filter=filter, offset_id=offset_id, limit=limit, saved_peer_id=saved_peer_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())
        
        b.write(self.filter.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()