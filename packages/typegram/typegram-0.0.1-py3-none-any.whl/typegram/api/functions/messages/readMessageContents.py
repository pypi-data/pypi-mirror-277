
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



class ReadMessageContents(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``36A73F77``

id (List of ``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.AffectedMessages<typegram.api.ayiin.messages.AffectedMessages>`
    """

    __slots__: List[str] = ["id"]

    ID = 0x36a73f77
    QUALNAME = "functions.functionsmessages.AffectedMessages"

    def __init__(self, *, id: List[int]) -> None:
        
                self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadMessageContents":
        # No flags
        
        id = Object.read(b, Int)
        
        return ReadMessageContents(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()