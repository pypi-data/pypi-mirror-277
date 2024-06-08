
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



class MessageActionPhoneCall(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``80E11A7F``

call_id (``int`` ``64-bit``):
                    N/A
                
        video (``bool``, *optional*):
                    N/A
                
        reason (:obj:`PhoneCallDiscardReason<typegram.api.ayiin.PhoneCallDiscardReason>`, *optional*):
                    N/A
                
        duration (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["call_id", "video", "reason", "duration"]

    ID = 0x80e11a7f
    QUALNAME = "types.messageActionPhoneCall"

    def __init__(self, *, call_id: int, video: Optional[bool] = None, reason: "api.ayiin.PhoneCallDiscardReason" = None, duration: Optional[int] = None) -> None:
        
                self.call_id = call_id  # long
        
                self.video = video  # true
        
                self.reason = reason  # PhoneCallDiscardReason
        
                self.duration = duration  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPhoneCall":
        
        flags = Int.read(b)
        
        video = True if flags & (1 << 2) else False
        call_id = Long.read(b)
        
        reason = Object.read(b) if flags & (1 << 0) else None
        
        duration = Int.read(b) if flags & (1 << 1) else None
        return MessageActionPhoneCall(call_id=call_id, video=video, reason=reason, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.call_id))
        
        if self.reason is not None:
            b.write(self.reason.write())
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        return b.getvalue()