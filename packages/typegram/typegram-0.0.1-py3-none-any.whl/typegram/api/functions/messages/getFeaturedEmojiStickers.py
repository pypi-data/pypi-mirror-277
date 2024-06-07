
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



class GetFeaturedEmojiStickers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``ECF6736``

hash (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`messages.FeaturedStickers<typegram.api.ayiin.messages.FeaturedStickers>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xecf6736
    QUALNAME = "functions.functionsmessages.FeaturedStickers"

    def __init__(self, *, hash: int) -> None:
        
                self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFeaturedEmojiStickers":
        # No flags
        
        hash = Long.read(b)
        
        return GetFeaturedEmojiStickers(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        return b.getvalue()