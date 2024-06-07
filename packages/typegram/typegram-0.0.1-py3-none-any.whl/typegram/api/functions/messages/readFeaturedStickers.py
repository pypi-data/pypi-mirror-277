
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



class ReadFeaturedStickers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``5B118126``

id (List of ``int`` ``64-bit``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id"]

    ID = 0x5b118126
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, id: List[int]) -> None:
        
                self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadFeaturedStickers":
        # No flags
        
        id = Object.read(b, Long)
        
        return ReadFeaturedStickers(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id, Long))
        
        return b.getvalue()