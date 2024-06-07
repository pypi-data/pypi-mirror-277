
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



class ConfirmPasswordEmail(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8FDF1920``

code (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["code"]

    ID = 0x8fdf1920
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, code: str) -> None:
        
                self.code = code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConfirmPasswordEmail":
        # No flags
        
        code = String.read(b)
        
        return ConfirmPasswordEmail(code=code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.code))
        
        return b.getvalue()