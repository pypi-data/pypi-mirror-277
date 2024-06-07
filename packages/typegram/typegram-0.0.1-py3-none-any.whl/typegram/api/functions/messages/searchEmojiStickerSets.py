
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



class SearchEmojiStickerSets(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``92B4494C``

q (``str``):
                    N/A
                
        hash (``int`` ``64-bit``):
                    N/A
                
        exclude_featured (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.FoundStickerSets<typegram.api.ayiin.messages.FoundStickerSets>`
    """

    __slots__: List[str] = ["q", "hash", "exclude_featured"]

    ID = 0x92b4494c
    QUALNAME = "functions.functionsmessages.FoundStickerSets"

    def __init__(self, *, q: str, hash: int, exclude_featured: Optional[bool] = None) -> None:
        
                self.q = q  # string
        
                self.hash = hash  # long
        
                self.exclude_featured = exclude_featured  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchEmojiStickerSets":
        
        flags = Int.read(b)
        
        exclude_featured = True if flags & (1 << 0) else False
        q = String.read(b)
        
        hash = Long.read(b)
        
        return SearchEmojiStickerSets(q=q, hash=hash, exclude_featured=exclude_featured)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.q))
        
        b.write(Long(self.hash))
        
        return b.getvalue()