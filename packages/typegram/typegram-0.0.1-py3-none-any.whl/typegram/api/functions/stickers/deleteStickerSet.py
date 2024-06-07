
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



class DeleteStickerSet(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``87704394``

stickerset (:obj:`InputStickerSet<typegram.api.ayiin.InputStickerSet>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["stickerset"]

    ID = 0x87704394
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, stickerset: "ayiin.InputStickerSet") -> None:
        
                self.stickerset = stickerset  # InputStickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteStickerSet":
        # No flags
        
        stickerset = Object.read(b)
        
        return DeleteStickerSet(stickerset=stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stickerset.write())
        
        return b.getvalue()