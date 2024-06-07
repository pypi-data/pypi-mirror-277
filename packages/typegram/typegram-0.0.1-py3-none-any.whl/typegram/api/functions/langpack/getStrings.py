
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



class GetStrings(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``EFEA3803``

lang_pack (``str``):
                    N/A
                
        lang_code (``str``):
                    N/A
                
        keys (List of ``str``):
                    N/A
                
    Returns:
        List of :obj:`LangPackString<typegram.api.ayiin.LangPackString>`
    """

    __slots__: List[str] = ["lang_pack", "lang_code", "keys"]

    ID = 0xefea3803
    QUALNAME = "functions.functions.Vector<LangPackString>"

    def __init__(self, *, lang_pack: str, lang_code: str, keys: List[str]) -> None:
        
                self.lang_pack = lang_pack  # string
        
                self.lang_code = lang_code  # string
        
                self.keys = keys  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStrings":
        # No flags
        
        lang_pack = String.read(b)
        
        lang_code = String.read(b)
        
        keys = Object.read(b, String)
        
        return GetStrings(lang_pack=lang_pack, lang_code=lang_code, keys=keys)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_pack))
        
        b.write(String(self.lang_code))
        
        b.write(Vector(self.keys, String))
        
        return b.getvalue()