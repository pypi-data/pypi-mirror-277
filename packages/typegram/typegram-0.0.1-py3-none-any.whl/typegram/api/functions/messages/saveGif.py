
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



class SaveGif(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``327A30CB``

id (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`):
                    N/A
                
        unsave (``bool``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "unsave"]

    ID = 0x327a30cb
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, id: "ayiin.InputDocument", unsave: bool) -> None:
        
                self.id = id  # InputDocument
        
                self.unsave = unsave  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveGif":
        # No flags
        
        id = Object.read(b)
        
        unsave = Bool.read(b)
        
        return SaveGif(id=id, unsave=unsave)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        b.write(Bool(self.unsave))
        
        return b.getvalue()