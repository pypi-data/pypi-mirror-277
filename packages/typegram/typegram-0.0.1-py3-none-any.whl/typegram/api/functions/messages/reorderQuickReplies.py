
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



class ReorderQuickReplies(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``60331907``

order (List of ``int`` ``32-bit``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["order"]

    ID = 0x60331907
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, order: List[int]) -> None:
        
                self.order = order  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderQuickReplies":
        # No flags
        
        order = Object.read(b, Int)
        
        return ReorderQuickReplies(order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.order, Int))
        
        return b.getvalue()