
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



class GetGroupParticipants(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``C558D8AB``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        ids (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        sources (List of ``int`` ``32-bit``):
                    N/A
                
        offset (``str``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`phone.GroupParticipants<typegram.api.ayiin.phone.GroupParticipants>`
    """

    __slots__: List[str] = ["call", "ids", "sources", "offset", "limit"]

    ID = 0xc558d8ab
    QUALNAME = "functions.functionsphone.GroupParticipants"

    def __init__(self, *, call: "ayiin.InputGroupCall", ids: List["ayiin.InputPeer"], sources: List[int], offset: str, limit: int) -> None:
        
                self.call = call  # InputGroupCall
        
                self.ids = ids  # InputPeer
        
                self.sources = sources  # int
        
                self.offset = offset  # string
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupParticipants":
        # No flags
        
        call = Object.read(b)
        
        ids = Object.read(b)
        
        sources = Object.read(b, Int)
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        return GetGroupParticipants(call=call, ids=ids, sources=sources, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Vector(self.ids))
        
        b.write(Vector(self.sources, Int))
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()