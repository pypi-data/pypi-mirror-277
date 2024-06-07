
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



class GetAppUpdate(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``522D5A7D``

source (``str``):
                    N/A
                
    Returns:
        :obj:`help.AppUpdate<typegram.api.ayiin.help.AppUpdate>`
    """

    __slots__: List[str] = ["source"]

    ID = 0x522d5a7d
    QUALNAME = "functions.functionshelp.AppUpdate"

    def __init__(self, *, source: str) -> None:
        
                self.source = source  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAppUpdate":
        # No flags
        
        source = String.read(b)
        
        return GetAppUpdate(source=source)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.source))
        
        return b.getvalue()