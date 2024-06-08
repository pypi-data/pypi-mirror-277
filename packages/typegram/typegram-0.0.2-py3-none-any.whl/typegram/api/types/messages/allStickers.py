
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



class AllStickers(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.AllStickers`.

    Details:
        - Layer: ``181``
        - ID: ``CDBBCEBB``

hash (``int`` ``64-bit``):
                    N/A
                
        sets (List of :obj:`StickerSet<typegram.api.ayiin.StickerSet>`):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getAllStickers
            messages.getMaskStickers
            messages.getEmojiStickers
    """

    __slots__: List[str] = ["hash", "sets"]

    ID = 0xcdbbcebb
    QUALNAME = "types.messages.allStickers"

    def __init__(self, *, hash: int, sets: List["api.ayiin.StickerSet"]) -> None:
        
                self.hash = hash  # long
        
                self.sets = sets  # StickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AllStickers":
        # No flags
        
        hash = Long.read(b)
        
        sets = Object.read(b)
        
        return AllStickers(hash=hash, sets=sets)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.sets))
        
        return b.getvalue()