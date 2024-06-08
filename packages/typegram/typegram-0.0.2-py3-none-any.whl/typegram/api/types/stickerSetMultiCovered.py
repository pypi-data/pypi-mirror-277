
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



class StickerSetMultiCovered(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StickerSetCovered`.

    Details:
        - Layer: ``181``
        - ID: ``3407E51B``

set (:obj:`StickerSet<typegram.api.ayiin.StickerSet>`):
                    N/A
                
        covers (List of :obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
    Functions:
        This object can be returned by 22 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getAttachedStickers
    """

    __slots__: List[str] = ["set", "covers"]

    ID = 0x3407e51b
    QUALNAME = "types.stickerSetMultiCovered"

    def __init__(self, *, set: "api.ayiin.StickerSet", covers: List["api.ayiin.Document"]) -> None:
        
                self.set = set  # StickerSet
        
                self.covers = covers  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSetMultiCovered":
        # No flags
        
        set = Object.read(b)
        
        covers = Object.read(b)
        
        return StickerSetMultiCovered(set=set, covers=covers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.set.write())
        
        b.write(Vector(self.covers))
        
        return b.getvalue()