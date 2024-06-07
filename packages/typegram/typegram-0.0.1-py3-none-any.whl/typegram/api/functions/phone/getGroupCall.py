
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



class GetGroupCall(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``41845DB``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`phone.GroupCall<typegram.api.ayiin.phone.GroupCall>`
    """

    __slots__: List[str] = ["call", "limit"]

    ID = 0x41845db
    QUALNAME = "functions.functionsphone.GroupCall"

    def __init__(self, *, call: "ayiin.InputGroupCall", limit: int) -> None:
        
                self.call = call  # InputGroupCall
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCall":
        # No flags
        
        call = Object.read(b)
        
        limit = Int.read(b)
        
        return GetGroupCall(call=call, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Int(self.limit))
        
        return b.getvalue()