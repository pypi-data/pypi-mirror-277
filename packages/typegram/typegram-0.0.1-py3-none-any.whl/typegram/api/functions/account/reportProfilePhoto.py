
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



class ReportProfilePhoto(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``FA8CC6F5``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        photo_id (:obj:`InputPhoto<typegram.api.ayiin.InputPhoto>`):
                    N/A
                
        reason (:obj:`ReportReason<typegram.api.ayiin.ReportReason>`):
                    N/A
                
        message (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "photo_id", "reason", "message"]

    ID = 0xfa8cc6f5
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", photo_id: "ayiin.InputPhoto", reason: "ayiin.ReportReason", message: str) -> None:
        
                self.peer = peer  # InputPeer
        
                self.photo_id = photo_id  # InputPhoto
        
                self.reason = reason  # ReportReason
        
                self.message = message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportProfilePhoto":
        # No flags
        
        peer = Object.read(b)
        
        photo_id = Object.read(b)
        
        reason = Object.read(b)
        
        message = String.read(b)
        
        return ReportProfilePhoto(peer=peer, photo_id=photo_id, reason=reason, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.photo_id.write())
        
        b.write(self.reason.write())
        
        b.write(String(self.message))
        
        return b.getvalue()