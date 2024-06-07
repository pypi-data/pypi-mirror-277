
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



class SendVerifyEmailCode(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``98E037BB``

purpose (:obj:`EmailVerifyPurpose<typegram.api.ayiin.EmailVerifyPurpose>`):
                    N/A
                
        email (``str``):
                    N/A
                
    Returns:
        :obj:`account.SentEmailCode<typegram.api.ayiin.account.SentEmailCode>`
    """

    __slots__: List[str] = ["purpose", "email"]

    ID = 0x98e037bb
    QUALNAME = "functions.functionsaccount.SentEmailCode"

    def __init__(self, *, purpose: "ayiin.EmailVerifyPurpose", email: str) -> None:
        
                self.purpose = purpose  # EmailVerifyPurpose
        
                self.email = email  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendVerifyEmailCode":
        # No flags
        
        purpose = Object.read(b)
        
        email = String.read(b)
        
        return SendVerifyEmailCode(purpose=purpose, email=email)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.purpose.write())
        
        b.write(String(self.email))
        
        return b.getvalue()