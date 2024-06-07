
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



class GetCountriesList(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``735787A8``

lang_code (``str``):
                    N/A
                
        hash (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`help.CountriesList<typegram.api.ayiin.help.CountriesList>`
    """

    __slots__: List[str] = ["lang_code", "hash"]

    ID = 0x735787a8
    QUALNAME = "functions.functionshelp.CountriesList"

    def __init__(self, *, lang_code: str, hash: int) -> None:
        
                self.lang_code = lang_code  # string
        
                self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCountriesList":
        # No flags
        
        lang_code = String.read(b)
        
        hash = Int.read(b)
        
        return GetCountriesList(lang_code=lang_code, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_code))
        
        b.write(Int(self.hash))
        
        return b.getvalue()