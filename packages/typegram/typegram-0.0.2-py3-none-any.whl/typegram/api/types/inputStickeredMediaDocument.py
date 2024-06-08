
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



class InputStickeredMediaDocument(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputStickeredMedia`.

    Details:
        - Layer: ``181``
        - ID: ``438865B``

id (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`):
                    N/A
                
    """

    __slots__: List[str] = ["id"]

    ID = 0x438865b
    QUALNAME = "types.inputStickeredMediaDocument"

    def __init__(self, *, id: "api.ayiin.InputDocument") -> None:
        
                self.id = id  # InputDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickeredMediaDocument":
        # No flags
        
        id = Object.read(b)
        
        return InputStickeredMediaDocument(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        return b.getvalue()