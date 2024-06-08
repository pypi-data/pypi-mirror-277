
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



class FeaturedStickersNotModified(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.FeaturedStickers`.

    Details:
        - Layer: ``181``
        - ID: ``C6DC0C66``

count (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 36 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getFeaturedStickers
            messages.getOldFeaturedStickers
            messages.getFeaturedEmojiStickers
    """

    __slots__: List[str] = ["count"]

    ID = 0xc6dc0c66
    QUALNAME = "types.messages.featuredStickersNotModified"

    def __init__(self, *, count: int) -> None:
        
                self.count = count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FeaturedStickersNotModified":
        # No flags
        
        count = Int.read(b)
        
        return FeaturedStickersNotModified(count=count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        return b.getvalue()