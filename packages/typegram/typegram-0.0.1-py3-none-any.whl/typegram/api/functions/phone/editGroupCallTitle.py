
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



class EditGroupCallTitle(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``1CA6AC0A``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        title (``str``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["call", "title"]

    ID = 0x1ca6ac0a
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, call: "ayiin.InputGroupCall", title: str) -> None:
        
                self.call = call  # InputGroupCall
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditGroupCallTitle":
        # No flags
        
        call = Object.read(b)
        
        title = String.read(b)
        
        return EditGroupCallTitle(call=call, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(String(self.title))
        
        return b.getvalue()