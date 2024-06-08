
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



class FavedStickers(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.FavedStickers`.

    Details:
        - Layer: ``181``
        - ID: ``2CB51097``

hash (``int`` ``64-bit``):
                    N/A
                
        packs (List of :obj:`StickerPack<typegram.api.ayiin.StickerPack>`):
                    N/A
                
        stickers (List of :obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
    Functions:
        This object can be returned by 22 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getFavedStickers
    """

    __slots__: List[str] = ["hash", "packs", "stickers"]

    ID = 0x2cb51097
    QUALNAME = "types.messages.favedStickers"

    def __init__(self, *, hash: int, packs: List["api.ayiin.StickerPack"], stickers: List["api.ayiin.Document"]) -> None:
        
                self.hash = hash  # long
        
                self.packs = packs  # StickerPack
        
                self.stickers = stickers  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FavedStickers":
        # No flags
        
        hash = Long.read(b)
        
        packs = Object.read(b)
        
        stickers = Object.read(b)
        
        return FavedStickers(hash=hash, packs=packs, stickers=stickers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.packs))
        
        b.write(Vector(self.stickers))
        
        return b.getvalue()