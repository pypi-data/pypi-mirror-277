
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



class CheckGroupCall(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B59CF977``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        sources (List of ``int`` ``32-bit``):
                    N/A
                
    Returns:
        List of ``int`` ``32-bit``
    """

    __slots__: List[str] = ["call", "sources"]

    ID = 0xb59cf977
    QUALNAME = "functions.functions.Vector<int>"

    def __init__(self, *, call: "ayiin.InputGroupCall", sources: List[int]) -> None:
        
                self.call = call  # InputGroupCall
        
                self.sources = sources  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckGroupCall":
        # No flags
        
        call = Object.read(b)
        
        sources = Object.read(b, Int)
        
        return CheckGroupCall(call=call, sources=sources)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Vector(self.sources, Int))
        
        return b.getvalue()