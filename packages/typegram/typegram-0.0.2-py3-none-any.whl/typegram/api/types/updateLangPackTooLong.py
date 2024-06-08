
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



class UpdateLangPackTooLong(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``46560264``

lang_code (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["lang_code"]

    ID = 0x46560264
    QUALNAME = "types.updateLangPackTooLong"

    def __init__(self, *, lang_code: str) -> None:
        
                self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateLangPackTooLong":
        # No flags
        
        lang_code = String.read(b)
        
        return UpdateLangPackTooLong(lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_code))
        
        return b.getvalue()