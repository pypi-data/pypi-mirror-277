
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



class LeaveGroupCall(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``500377F9``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        source (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["call", "source"]

    ID = 0x500377f9
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, call: "ayiin.InputGroupCall", source: int) -> None:
        
                self.call = call  # InputGroupCall
        
                self.source = source  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LeaveGroupCall":
        # No flags
        
        call = Object.read(b)
        
        source = Int.read(b)
        
        return LeaveGroupCall(call=call, source=source)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Int(self.source))
        
        return b.getvalue()