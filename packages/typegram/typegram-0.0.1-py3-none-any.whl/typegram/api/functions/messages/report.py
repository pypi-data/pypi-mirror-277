
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



class Report(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8953AB4E``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (List of ``int`` ``32-bit``):
                    N/A
                
        reason (:obj:`ReportReason<typegram.api.ayiin.ReportReason>`):
                    N/A
                
        message (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "id", "reason", "message"]

    ID = 0x8953ab4e
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", id: List[int], reason: "ayiin.ReportReason", message: str) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.reason = reason  # ReportReason
        
                self.message = message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Report":
        # No flags
        
        peer = Object.read(b)
        
        id = Object.read(b, Int)
        
        reason = Object.read(b)
        
        message = String.read(b)
        
        return Report(peer=peer, id=id, reason=reason, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.id, Int))
        
        b.write(self.reason.write())
        
        b.write(String(self.message))
        
        return b.getvalue()