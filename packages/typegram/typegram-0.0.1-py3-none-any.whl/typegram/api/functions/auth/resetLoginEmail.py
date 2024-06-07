
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



class ResetLoginEmail(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``7E960193``

phone_number (``str``):
                    N/A
                
        phone_code_hash (``str``):
                    N/A
                
    Returns:
        :obj:`auth.SentCode<typegram.api.ayiin.auth.SentCode>`
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash"]

    ID = 0x7e960193
    QUALNAME = "functions.functionsauth.SentCode"

    def __init__(self, *, phone_number: str, phone_code_hash: str) -> None:
        
                self.phone_number = phone_number  # string
        
                self.phone_code_hash = phone_code_hash  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetLoginEmail":
        # No flags
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        return ResetLoginEmail(phone_number=phone_number, phone_code_hash=phone_code_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        return b.getvalue()