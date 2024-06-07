
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



class GetDifference(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``CD984AA5``

lang_pack (``str``):
                    N/A
                
        lang_code (``str``):
                    N/A
                
        from_version (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`LangPackDifference<typegram.api.ayiin.LangPackDifference>`
    """

    __slots__: List[str] = ["lang_pack", "lang_code", "from_version"]

    ID = 0xcd984aa5
    QUALNAME = "functions.functions.LangPackDifference"

    def __init__(self, *, lang_pack: str, lang_code: str, from_version: int) -> None:
        
                self.lang_pack = lang_pack  # string
        
                self.lang_code = lang_code  # string
        
                self.from_version = from_version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDifference":
        # No flags
        
        lang_pack = String.read(b)
        
        lang_code = String.read(b)
        
        from_version = Int.read(b)
        
        return GetDifference(lang_pack=lang_pack, lang_code=lang_code, from_version=from_version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_pack))
        
        b.write(String(self.lang_code))
        
        b.write(Int(self.from_version))
        
        return b.getvalue()