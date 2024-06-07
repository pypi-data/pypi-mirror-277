
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



class DeletePhotos(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``87CF7F2F``

id (List of :obj:`InputPhoto<typegram.api.ayiin.InputPhoto>`):
                    N/A
                
    Returns:
        List of ``int`` ``64-bit``
    """

    __slots__: List[str] = ["id"]

    ID = 0x87cf7f2f
    QUALNAME = "functions.functions.Vector<long>"

    def __init__(self, *, id: List["ayiin.InputPhoto"]) -> None:
        
                self.id = id  # InputPhoto

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeletePhotos":
        # No flags
        
        id = Object.read(b)
        
        return DeletePhotos(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id))
        
        return b.getvalue()