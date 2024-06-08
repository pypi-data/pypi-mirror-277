
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



class MessageActionGroupCall(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``7A0D7F42``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        duration (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["call", "duration"]

    ID = 0x7a0d7f42
    QUALNAME = "types.messageActionGroupCall"

    def __init__(self, *, call: "api.ayiin.InputGroupCall", duration: Optional[int] = None) -> None:
        
                self.call = call  # InputGroupCall
        
                self.duration = duration  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGroupCall":
        
        flags = Int.read(b)
        
        call = Object.read(b)
        
        duration = Int.read(b) if flags & (1 << 0) else None
        return MessageActionGroupCall(call=call, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        return b.getvalue()