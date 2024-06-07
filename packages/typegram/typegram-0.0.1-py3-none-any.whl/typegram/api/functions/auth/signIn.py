
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



class SignIn(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8D52A951``

phone_number (``str``):
                    N/A
                
        phone_code_hash (``str``):
                    N/A
                
        phone_code (``str``, *optional*):
                    N/A
                
        email_verification (:obj:`EmailVerification<typegram.api.ayiin.EmailVerification>`, *optional*):
                    N/A
                
    Returns:
        :obj:`auth.Authorization<typegram.api.ayiin.auth.Authorization>`
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "phone_code", "email_verification"]

    ID = 0x8d52a951
    QUALNAME = "functions.functionsauth.Authorization"

    def __init__(self, *, phone_number: str, phone_code_hash: str, phone_code: Optional[str] = None, email_verification: "ayiin.EmailVerification" = None) -> None:
        
                self.phone_number = phone_number  # string
        
                self.phone_code_hash = phone_code_hash  # string
        
                self.phone_code = phone_code  # string
        
                self.email_verification = email_verification  # EmailVerification

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SignIn":
        
        flags = Int.read(b)
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        phone_code = String.read(b) if flags & (1 << 0) else None
        email_verification = Object.read(b) if flags & (1 << 1) else None
        
        return SignIn(phone_number=phone_number, phone_code_hash=phone_code_hash, phone_code=phone_code, email_verification=email_verification)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        if self.phone_code is not None:
            b.write(String(self.phone_code))
        
        if self.email_verification is not None:
            b.write(self.email_verification.write())
        
        return b.getvalue()