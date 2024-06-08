
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



class EmojiKeywordDeleted(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.EmojiKeyword`.

    Details:
        - Layer: ``181``
        - ID: ``236DF622``

keyword (``str``):
                    N/A
                
        emoticons (List of ``str``):
                    N/A
                
    """

    __slots__: List[str] = ["keyword", "emoticons"]

    ID = 0x236df622
    QUALNAME = "types.emojiKeywordDeleted"

    def __init__(self, *, keyword: str, emoticons: List[str]) -> None:
        
                self.keyword = keyword  # string
        
                self.emoticons = emoticons  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiKeywordDeleted":
        # No flags
        
        keyword = String.read(b)
        
        emoticons = Object.read(b, String)
        
        return EmojiKeywordDeleted(keyword=keyword, emoticons=emoticons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.keyword))
        
        b.write(Vector(self.emoticons, String))
        
        return b.getvalue()