
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



class GetStarsTransactions(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``673AC2F9``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        offset (``str``):
                    N/A
                
        inbound (``bool``, *optional*):
                    N/A
                
        outbound (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`payments.StarsStatus<typegram.api.ayiin.payments.StarsStatus>`
    """

    __slots__: List[str] = ["peer", "offset", "inbound", "outbound"]

    ID = 0x673ac2f9
    QUALNAME = "functions.functionspayments.StarsStatus"

    def __init__(self, *, peer: "ayiin.InputPeer", offset: str, inbound: Optional[bool] = None, outbound: Optional[bool] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.offset = offset  # string
        
                self.inbound = inbound  # true
        
                self.outbound = outbound  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsTransactions":
        
        flags = Int.read(b)
        
        inbound = True if flags & (1 << 0) else False
        outbound = True if flags & (1 << 1) else False
        peer = Object.read(b)
        
        offset = String.read(b)
        
        return GetStarsTransactions(peer=peer, offset=offset, inbound=inbound, outbound=outbound)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.offset))
        
        return b.getvalue()