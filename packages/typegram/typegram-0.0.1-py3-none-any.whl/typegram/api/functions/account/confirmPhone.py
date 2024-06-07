
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



class ConfirmPhone(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``5F2178C3``

phone_code_hash (``str``):
                    N/A
                
        phone_code (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_code_hash", "phone_code"]

    ID = 0x5f2178c3
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, phone_code_hash: str, phone_code: str) -> None:
        
                self.phone_code_hash = phone_code_hash  # string
        
                self.phone_code = phone_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConfirmPhone":
        # No flags
        
        phone_code_hash = String.read(b)
        
        phone_code = String.read(b)
        
        return ConfirmPhone(phone_code_hash=phone_code_hash, phone_code=phone_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.phone_code_hash))
        
        b.write(String(self.phone_code))
        
        return b.getvalue()