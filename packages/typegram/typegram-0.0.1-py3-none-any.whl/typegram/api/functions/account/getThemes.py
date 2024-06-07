
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



class GetThemes(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``7206E458``

format (``str``):
                    N/A
                
        hash (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`account.Themes<typegram.api.ayiin.account.Themes>`
    """

    __slots__: List[str] = ["format", "hash"]

    ID = 0x7206e458
    QUALNAME = "functions.functionsaccount.Themes"

    def __init__(self, *, format: str, hash: int) -> None:
        
                self.format = format  # string
        
                self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetThemes":
        # No flags
        
        format = String.read(b)
        
        hash = Long.read(b)
        
        return GetThemes(format=format, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.format))
        
        b.write(Long(self.hash))
        
        return b.getvalue()