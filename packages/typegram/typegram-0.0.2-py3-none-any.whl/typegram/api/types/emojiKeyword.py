
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



class EmojiKeyword(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.EmojiKeyword`.

    Details:
        - Layer: ``181``
        - ID: ``D5B3B9F9``

keyword (``str``):
                    N/A
                
        emoticons (List of ``str``):
                    N/A
                
    """

    __slots__: List[str] = ["keyword", "emoticons"]

    ID = 0xd5b3b9f9
    QUALNAME = "types.emojiKeyword"

    def __init__(self, *, keyword: str, emoticons: List[str]) -> None:
        
                self.keyword = keyword  # string
        
                self.emoticons = emoticons  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiKeyword":
        # No flags
        
        keyword = String.read(b)
        
        emoticons = Object.read(b, String)
        
        return EmojiKeyword(keyword=keyword, emoticons=emoticons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.keyword))
        
        b.write(Vector(self.emoticons, String))
        
        return b.getvalue()