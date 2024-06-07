
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



class GetLanguages(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``42C6978F``

lang_pack (``str``):
                    N/A
                
    Returns:
        List of :obj:`LangPackLanguage<typegram.api.ayiin.LangPackLanguage>`
    """

    __slots__: List[str] = ["lang_pack"]

    ID = 0x42c6978f
    QUALNAME = "functions.functions.Vector<LangPackLanguage>"

    def __init__(self, *, lang_pack: str) -> None:
        
                self.lang_pack = lang_pack  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetLanguages":
        # No flags
        
        lang_pack = String.read(b)
        
        return GetLanguages(lang_pack=lang_pack)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_pack))
        
        return b.getvalue()