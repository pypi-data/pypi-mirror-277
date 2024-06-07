
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



class EditCloseFriends(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``BA6705F0``

id (List of ``int`` ``64-bit``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id"]

    ID = 0xba6705f0
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, id: List[int]) -> None:
        
                self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditCloseFriends":
        # No flags
        
        id = Object.read(b, Long)
        
        return EditCloseFriends(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id, Long))
        
        return b.getvalue()