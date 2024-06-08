
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



class MyStickers(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.MyStickers`.

    Details:
        - Layer: ``181``
        - ID: ``FAFF629D``

count (``int`` ``32-bit``):
                    N/A
                
        sets (List of :obj:`StickerSetCovered<typegram.api.ayiin.StickerSetCovered>`):
                    N/A
                
    Functions:
        This object can be returned by 19 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getMyStickers
    """

    __slots__: List[str] = ["count", "sets"]

    ID = 0xfaff629d
    QUALNAME = "types.messages.myStickers"

    def __init__(self, *, count: int, sets: List["api.ayiin.StickerSetCovered"]) -> None:
        
                self.count = count  # int
        
                self.sets = sets  # StickerSetCovered

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MyStickers":
        # No flags
        
        count = Int.read(b)
        
        sets = Object.read(b)
        
        return MyStickers(count=count, sets=sets)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.sets))
        
        return b.getvalue()