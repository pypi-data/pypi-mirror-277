
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



class InputWallPaperNoFile(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputWallPaper`.

    Details:
        - Layer: ``181``
        - ID: ``967A462E``

id (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["id"]

    ID = 0x967a462e
    QUALNAME = "types.inputWallPaperNoFile"

    def __init__(self, *, id: int) -> None:
        
                self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWallPaperNoFile":
        # No flags
        
        id = Long.read(b)
        
        return InputWallPaperNoFile(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        return b.getvalue()