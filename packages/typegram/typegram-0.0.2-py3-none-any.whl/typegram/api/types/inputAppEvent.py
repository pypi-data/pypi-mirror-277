
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



class InputAppEvent(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputAppEvent`.

    Details:
        - Layer: ``181``
        - ID: ``1D1B1245``

time (``float`` ``64-bit``):
                    N/A
                
        type (``str``):
                    N/A
                
        peer (``int`` ``64-bit``):
                    N/A
                
        data (:obj:`JSONValue<typegram.api.ayiin.JSONValue>`):
                    N/A
                
    """

    __slots__: List[str] = ["time", "type", "peer", "data"]

    ID = 0x1d1b1245
    QUALNAME = "types.inputAppEvent"

    def __init__(self, *, time: float, type: str, peer: int, data: "api.ayiin.JSONValue") -> None:
        
                self.time = time  # double
        
                self.type = type  # string
        
                self.peer = peer  # long
        
                self.data = data  # JSONValue

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputAppEvent":
        # No flags
        
        time = Double.read(b)
        
        type = String.read(b)
        
        peer = Long.read(b)
        
        data = Object.read(b)
        
        return InputAppEvent(time=time, type=type, peer=peer, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Double(self.time))
        
        b.write(String(self.type))
        
        b.write(Long(self.peer))
        
        b.write(self.data.write())
        
        return b.getvalue()