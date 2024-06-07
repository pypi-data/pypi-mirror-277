
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



class FaveSticker(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B9FFC55B``

id (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`):
                    N/A
                
        unfave (``bool``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "unfave"]

    ID = 0xb9ffc55b
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, id: "ayiin.InputDocument", unfave: bool) -> None:
        
                self.id = id  # InputDocument
        
                self.unfave = unfave  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FaveSticker":
        # No flags
        
        id = Object.read(b)
        
        unfave = Bool.read(b)
        
        return FaveSticker(id=id, unfave=unfave)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        b.write(Bool(self.unfave))
        
        return b.getvalue()