
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



class EmojiKeywordsDifference(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.EmojiKeywordsDifference`.

    Details:
        - Layer: ``181``
        - ID: ``5CC761BD``

lang_code (``str``):
                    N/A
                
        from_version (``int`` ``32-bit``):
                    N/A
                
        version (``int`` ``32-bit``):
                    N/A
                
        keywords (List of :obj:`EmojiKeyword<typegram.api.ayiin.EmojiKeyword>`):
                    N/A
                
    Functions:
        This object can be returned by 23 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getEmojiKeywords
            messages.getEmojiKeywordsDifference
    """

    __slots__: List[str] = ["lang_code", "from_version", "version", "keywords"]

    ID = 0x5cc761bd
    QUALNAME = "types.emojiKeywordsDifference"

    def __init__(self, *, lang_code: str, from_version: int, version: int, keywords: List["api.ayiin.EmojiKeyword"]) -> None:
        
                self.lang_code = lang_code  # string
        
                self.from_version = from_version  # int
        
                self.version = version  # int
        
                self.keywords = keywords  # EmojiKeyword

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiKeywordsDifference":
        # No flags
        
        lang_code = String.read(b)
        
        from_version = Int.read(b)
        
        version = Int.read(b)
        
        keywords = Object.read(b)
        
        return EmojiKeywordsDifference(lang_code=lang_code, from_version=from_version, version=version, keywords=keywords)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_code))
        
        b.write(Int(self.from_version))
        
        b.write(Int(self.version))
        
        b.write(Vector(self.keywords))
        
        return b.getvalue()