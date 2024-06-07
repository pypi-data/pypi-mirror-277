
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



class CheckShortName(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``284B3639``

short_name (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["short_name"]

    ID = 0x284b3639
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, short_name: str) -> None:
        
                self.short_name = short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckShortName":
        # No flags
        
        short_name = String.read(b)
        
        return CheckShortName(short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.short_name))
        
        return b.getvalue()