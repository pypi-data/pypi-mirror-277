
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



class ResendCode(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``CAE47523``

phone_number (``str``):
                    N/A
                
        phone_code_hash (``str``):
                    N/A
                
        reason (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`auth.SentCode<typegram.api.ayiin.auth.SentCode>`
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "reason"]

    ID = 0xcae47523
    QUALNAME = "functions.functionsauth.SentCode"

    def __init__(self, *, phone_number: str, phone_code_hash: str, reason: Optional[str] = None) -> None:
        
                self.phone_number = phone_number  # string
        
                self.phone_code_hash = phone_code_hash  # string
        
                self.reason = reason  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResendCode":
        
        flags = Int.read(b)
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        reason = String.read(b) if flags & (1 << 0) else None
        return ResendCode(phone_number=phone_number, phone_code_hash=phone_code_hash, reason=reason)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        if self.reason is not None:
            b.write(String(self.reason))
        
        return b.getvalue()