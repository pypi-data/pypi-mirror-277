
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



class DiscardCall(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B2CBC1C0``

peer (:obj:`InputPhoneCall<typegram.api.ayiin.InputPhoneCall>`):
                    N/A
                
        duration (``int`` ``32-bit``):
                    N/A
                
        reason (:obj:`PhoneCallDiscardReason<typegram.api.ayiin.PhoneCallDiscardReason>`):
                    N/A
                
        connection_id (``int`` ``64-bit``):
                    N/A
                
        video (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "duration", "reason", "connection_id", "video"]

    ID = 0xb2cbc1c0
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPhoneCall", duration: int, reason: "ayiin.PhoneCallDiscardReason", connection_id: int, video: Optional[bool] = None) -> None:
        
                self.peer = peer  # InputPhoneCall
        
                self.duration = duration  # int
        
                self.reason = reason  # PhoneCallDiscardReason
        
                self.connection_id = connection_id  # long
        
                self.video = video  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DiscardCall":
        
        flags = Int.read(b)
        
        video = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        duration = Int.read(b)
        
        reason = Object.read(b)
        
        connection_id = Long.read(b)
        
        return DiscardCall(peer=peer, duration=duration, reason=reason, connection_id=connection_id, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.duration))
        
        b.write(self.reason.write())
        
        b.write(Long(self.connection_id))
        
        return b.getvalue()