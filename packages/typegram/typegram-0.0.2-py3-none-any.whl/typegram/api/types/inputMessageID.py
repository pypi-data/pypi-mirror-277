
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



class InputMessageID(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputMessage`.

    Details:
        - Layer: ``181``
        - ID: ``A676A322``

id (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["id"]

    ID = 0xa676a322
    QUALNAME = "types.inputMessageID"

    def __init__(self, *, id: int) -> None:
        
                self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessageID":
        # No flags
        
        id = Int.read(b)
        
        return InputMessageID(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.id))
        
        return b.getvalue()