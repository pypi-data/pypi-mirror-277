
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



class RecentStickers(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.RecentStickers`.

    Details:
        - Layer: ``181``
        - ID: ``88D37C56``

hash (``int`` ``64-bit``):
                    N/A
                
        packs (List of :obj:`StickerPack<typegram.api.ayiin.StickerPack>`):
                    N/A
                
        stickers (List of :obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
        dates (List of ``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 23 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getRecentStickers
    """

    __slots__: List[str] = ["hash", "packs", "stickers", "dates"]

    ID = 0x88d37c56
    QUALNAME = "types.messages.recentStickers"

    def __init__(self, *, hash: int, packs: List["api.ayiin.StickerPack"], stickers: List["api.ayiin.Document"], dates: List[int]) -> None:
        
                self.hash = hash  # long
        
                self.packs = packs  # StickerPack
        
                self.stickers = stickers  # Document
        
                self.dates = dates  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecentStickers":
        # No flags
        
        hash = Long.read(b)
        
        packs = Object.read(b)
        
        stickers = Object.read(b)
        
        dates = Object.read(b, Int)
        
        return RecentStickers(hash=hash, packs=packs, stickers=stickers, dates=dates)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.packs))
        
        b.write(Vector(self.stickers))
        
        b.write(Vector(self.dates, Int))
        
        return b.getvalue()