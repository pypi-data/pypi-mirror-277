
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



class VerifyEmail(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``32DA4CF``

purpose (:obj:`EmailVerifyPurpose<typegram.api.ayiin.EmailVerifyPurpose>`):
                    N/A
                
        verification (:obj:`EmailVerification<typegram.api.ayiin.EmailVerification>`):
                    N/A
                
    Returns:
        :obj:`account.EmailVerified<typegram.api.ayiin.account.EmailVerified>`
    """

    __slots__: List[str] = ["purpose", "verification"]

    ID = 0x32da4cf
    QUALNAME = "functions.functionsaccount.EmailVerified"

    def __init__(self, *, purpose: "ayiin.EmailVerifyPurpose", verification: "ayiin.EmailVerification") -> None:
        
                self.purpose = purpose  # EmailVerifyPurpose
        
                self.verification = verification  # EmailVerification

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VerifyEmail":
        # No flags
        
        purpose = Object.read(b)
        
        verification = Object.read(b)
        
        return VerifyEmail(purpose=purpose, verification=verification)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.purpose.write())
        
        b.write(self.verification.write())
        
        return b.getvalue()