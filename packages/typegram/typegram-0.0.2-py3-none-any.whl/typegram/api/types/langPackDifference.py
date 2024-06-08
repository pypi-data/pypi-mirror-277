
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



class LangPackDifference(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.LangPackDifference`.

    Details:
        - Layer: ``181``
        - ID: ``F385C1F6``

lang_code (``str``):
                    N/A
                
        from_version (``int`` ``32-bit``):
                    N/A
                
        version (``int`` ``32-bit``):
                    N/A
                
        strings (List of :obj:`LangPackString<typegram.api.ayiin.LangPackString>`):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            langpack.getLangPack
            langpack.getDifference
    """

    __slots__: List[str] = ["lang_code", "from_version", "version", "strings"]

    ID = 0xf385c1f6
    QUALNAME = "types.langPackDifference"

    def __init__(self, *, lang_code: str, from_version: int, version: int, strings: List["api.ayiin.LangPackString"]) -> None:
        
                self.lang_code = lang_code  # string
        
                self.from_version = from_version  # int
        
                self.version = version  # int
        
                self.strings = strings  # LangPackString

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LangPackDifference":
        # No flags
        
        lang_code = String.read(b)
        
        from_version = Int.read(b)
        
        version = Int.read(b)
        
        strings = Object.read(b)
        
        return LangPackDifference(lang_code=lang_code, from_version=from_version, version=version, strings=strings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_code))
        
        b.write(Int(self.from_version))
        
        b.write(Int(self.version))
        
        b.write(Vector(self.strings))
        
        return b.getvalue()