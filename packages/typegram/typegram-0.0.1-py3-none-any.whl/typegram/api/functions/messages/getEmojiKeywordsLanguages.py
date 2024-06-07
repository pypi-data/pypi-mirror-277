
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



class GetEmojiKeywordsLanguages(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``4E9963B2``

lang_codes (List of ``str``):
                    N/A
                
    Returns:
        List of :obj:`EmojiLanguage<typegram.api.ayiin.EmojiLanguage>`
    """

    __slots__: List[str] = ["lang_codes"]

    ID = 0x4e9963b2
    QUALNAME = "functions.functions.Vector<EmojiLanguage>"

    def __init__(self, *, lang_codes: List[str]) -> None:
        
                self.lang_codes = lang_codes  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetEmojiKeywordsLanguages":
        # No flags
        
        lang_codes = Object.read(b, String)
        
        return GetEmojiKeywordsLanguages(lang_codes=lang_codes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.lang_codes, String))
        
        return b.getvalue()