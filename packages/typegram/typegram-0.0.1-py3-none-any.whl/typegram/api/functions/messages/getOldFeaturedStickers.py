
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



class GetOldFeaturedStickers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``7ED094A1``

offset (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        hash (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`messages.FeaturedStickers<typegram.api.ayiin.messages.FeaturedStickers>`
    """

    __slots__: List[str] = ["offset", "limit", "hash"]

    ID = 0x7ed094a1
    QUALNAME = "functions.functionsmessages.FeaturedStickers"

    def __init__(self, *, offset: int, limit: int, hash: int) -> None:
        
                self.offset = offset  # int
        
                self.limit = limit  # int
        
                self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetOldFeaturedStickers":
        # No flags
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetOldFeaturedStickers(offset=offset, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()