
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



class DocumentAttributeImageSize(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.DocumentAttribute`.

    Details:
        - Layer: ``181``
        - ID: ``6C37C15C``

w (``int`` ``32-bit``):
                    N/A
                
        h (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["w", "h"]

    ID = 0x6c37c15c
    QUALNAME = "types.documentAttributeImageSize"

    def __init__(self, *, w: int, h: int) -> None:
        
                self.w = w  # int
        
                self.h = h  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeImageSize":
        # No flags
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        return DocumentAttributeImageSize(w=w, h=h)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        return b.getvalue()