
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



class SearchGlobal(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``4BC6589A``

q (``str``):
                    N/A
                
        filter (:obj:`MessagesFilter<typegram.api.ayiin.MessagesFilter>`):
                    N/A
                
        min_date (``int`` ``32-bit``):
                    N/A
                
        max_date (``int`` ``32-bit``):
                    N/A
                
        offset_rate (``int`` ``32-bit``):
                    N/A
                
        offset_peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        offset_id (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        broadcasts_only (``bool``, *optional*):
                    N/A
                
        folder_id (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.Messages<typegram.api.ayiin.messages.Messages>`
    """

    __slots__: List[str] = ["q", "filter", "min_date", "max_date", "offset_rate", "offset_peer", "offset_id", "limit", "broadcasts_only", "folder_id"]

    ID = 0x4bc6589a
    QUALNAME = "functions.functionsmessages.Messages"

    def __init__(self, *, q: str, filter: "ayiin.MessagesFilter", min_date: int, max_date: int, offset_rate: int, offset_peer: "ayiin.InputPeer", offset_id: int, limit: int, broadcasts_only: Optional[bool] = None, folder_id: Optional[int] = None) -> None:
        
                self.q = q  # string
        
                self.filter = filter  # MessagesFilter
        
                self.min_date = min_date  # int
        
                self.max_date = max_date  # int
        
                self.offset_rate = offset_rate  # int
        
                self.offset_peer = offset_peer  # InputPeer
        
                self.offset_id = offset_id  # int
        
                self.limit = limit  # int
        
                self.broadcasts_only = broadcasts_only  # true
        
                self.folder_id = folder_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchGlobal":
        
        flags = Int.read(b)
        
        broadcasts_only = True if flags & (1 << 1) else False
        folder_id = Int.read(b) if flags & (1 << 0) else None
        q = String.read(b)
        
        filter = Object.read(b)
        
        min_date = Int.read(b)
        
        max_date = Int.read(b)
        
        offset_rate = Int.read(b)
        
        offset_peer = Object.read(b)
        
        offset_id = Int.read(b)
        
        limit = Int.read(b)
        
        return SearchGlobal(q=q, filter=filter, min_date=min_date, max_date=max_date, offset_rate=offset_rate, offset_peer=offset_peer, offset_id=offset_id, limit=limit, broadcasts_only=broadcasts_only, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        b.write(String(self.q))
        
        b.write(self.filter.write())
        
        b.write(Int(self.min_date))
        
        b.write(Int(self.max_date))
        
        b.write(Int(self.offset_rate))
        
        b.write(self.offset_peer.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()