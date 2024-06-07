
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



class CancelCode(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``1F040578``

phone_number (``str``):
                    N/A
                
        phone_code_hash (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash"]

    ID = 0x1f040578
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, phone_number: str, phone_code_hash: str) -> None:
        
                self.phone_number = phone_number  # string
        
                self.phone_code_hash = phone_code_hash  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CancelCode":
        # No flags
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        return CancelCode(phone_number=phone_number, phone_code_hash=phone_code_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        return b.getvalue()