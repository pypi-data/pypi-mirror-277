
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



class UpdateBotInlineQuery(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``496F379C``

query_id (``int`` ``64-bit``):
                    N/A
                
        user_id (``int`` ``64-bit``):
                    N/A
                
        query (``str``):
                    N/A
                
        offset (``str``):
                    N/A
                
        geo (:obj:`GeoPoint<typegram.api.ayiin.GeoPoint>`, *optional*):
                    N/A
                
        peer_type (:obj:`InlineQueryPeerType<typegram.api.ayiin.InlineQueryPeerType>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["query_id", "user_id", "query", "offset", "geo", "peer_type"]

    ID = 0x496f379c
    QUALNAME = "types.updateBotInlineQuery"

    def __init__(self, *, query_id: int, user_id: int, query: str, offset: str, geo: "api.ayiin.GeoPoint" = None, peer_type: "api.ayiin.InlineQueryPeerType" = None) -> None:
        
                self.query_id = query_id  # long
        
                self.user_id = user_id  # long
        
                self.query = query  # string
        
                self.offset = offset  # string
        
                self.geo = geo  # GeoPoint
        
                self.peer_type = peer_type  # InlineQueryPeerType

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotInlineQuery":
        
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        user_id = Long.read(b)
        
        query = String.read(b)
        
        geo = Object.read(b) if flags & (1 << 0) else None
        
        peer_type = Object.read(b) if flags & (1 << 1) else None
        
        offset = String.read(b)
        
        return UpdateBotInlineQuery(query_id=query_id, user_id=user_id, query=query, offset=offset, geo=geo, peer_type=peer_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        b.write(Long(self.user_id))
        
        b.write(String(self.query))
        
        if self.geo is not None:
            b.write(self.geo.write())
        
        if self.peer_type is not None:
            b.write(self.peer_type.write())
        
        b.write(String(self.offset))
        
        return b.getvalue()