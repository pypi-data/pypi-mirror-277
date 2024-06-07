
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



class InvalidateSignInCodes(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``CA8AE8BA``

codes (List of ``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["codes"]

    ID = 0xca8ae8ba
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, codes: List[str]) -> None:
        
                self.codes = codes  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvalidateSignInCodes":
        # No flags
        
        codes = Object.read(b, String)
        
        return InvalidateSignInCodes(codes=codes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.codes, String))
        
        return b.getvalue()