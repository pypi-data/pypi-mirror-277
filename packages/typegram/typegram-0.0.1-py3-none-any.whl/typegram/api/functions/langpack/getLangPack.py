
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



class GetLangPack(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F2F2330A``

lang_pack (``str``):
                    N/A
                
        lang_code (``str``):
                    N/A
                
    Returns:
        :obj:`LangPackDifference<typegram.api.ayiin.LangPackDifference>`
    """

    __slots__: List[str] = ["lang_pack", "lang_code"]

    ID = 0xf2f2330a
    QUALNAME = "functions.functions.LangPackDifference"

    def __init__(self, *, lang_pack: str, lang_code: str) -> None:
        
                self.lang_pack = lang_pack  # string
        
                self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetLangPack":
        # No flags
        
        lang_pack = String.read(b)
        
        lang_code = String.read(b)
        
        return GetLangPack(lang_pack=lang_pack, lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_pack))
        
        b.write(String(self.lang_code))
        
        return b.getvalue()