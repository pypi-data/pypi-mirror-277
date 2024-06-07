
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



class GetBoostsList(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``60F67660``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        offset (``str``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        gifts (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`premium.BoostsList<typegram.api.ayiin.premium.BoostsList>`
    """

    __slots__: List[str] = ["peer", "offset", "limit", "gifts"]

    ID = 0x60f67660
    QUALNAME = "functions.functionspremium.BoostsList"

    def __init__(self, *, peer: "ayiin.InputPeer", offset: str, limit: int, gifts: Optional[bool] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.offset = offset  # string
        
                self.limit = limit  # int
        
                self.gifts = gifts  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBoostsList":
        
        flags = Int.read(b)
        
        gifts = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        return GetBoostsList(peer=peer, offset=offset, limit=limit, gifts=gifts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()