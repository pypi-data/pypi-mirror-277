
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



class FeaturedStickers(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.FeaturedStickers`.

    Details:
        - Layer: ``181``
        - ID: ``BE382906``

hash (``int`` ``64-bit``):
                    N/A
                
        count (``int`` ``32-bit``):
                    N/A
                
        sets (List of :obj:`StickerSetCovered<typegram.api.ayiin.StickerSetCovered>`):
                    N/A
                
        unread (List of ``int`` ``64-bit``):
                    N/A
                
        premium (``bool``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 25 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getFeaturedStickers
            messages.getOldFeaturedStickers
            messages.getFeaturedEmojiStickers
    """

    __slots__: List[str] = ["hash", "count", "sets", "unread", "premium"]

    ID = 0xbe382906
    QUALNAME = "types.messages.featuredStickers"

    def __init__(self, *, hash: int, count: int, sets: List["api.ayiin.StickerSetCovered"], unread: List[int], premium: Optional[bool] = None) -> None:
        
                self.hash = hash  # long
        
                self.count = count  # int
        
                self.sets = sets  # StickerSetCovered
        
                self.unread = unread  # long
        
                self.premium = premium  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FeaturedStickers":
        
        flags = Int.read(b)
        
        premium = True if flags & (1 << 0) else False
        hash = Long.read(b)
        
        count = Int.read(b)
        
        sets = Object.read(b)
        
        unread = Object.read(b, Long)
        
        return FeaturedStickers(hash=hash, count=count, sets=sets, unread=unread, premium=premium)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.hash))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.sets))
        
        b.write(Vector(self.unread, Long))
        
        return b.getvalue()