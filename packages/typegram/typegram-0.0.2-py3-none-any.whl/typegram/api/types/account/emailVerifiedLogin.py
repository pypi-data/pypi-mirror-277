
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class EmailVerifiedLogin(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.EmailVerified`.

    Details:
        - Layer: ``181``
        - ID: ``E1BB0D61``

email (``str``):
                    N/A
                
        sent_code (:obj:`auth.SentCode<typegram.api.ayiin.auth.SentCode>`):
                    N/A
                
    Functions:
        This object can be returned by 26 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            account.verifyEmail
    """

    __slots__: List[str] = ["email", "sent_code"]

    ID = 0xe1bb0d61
    QUALNAME = "types.account.emailVerifiedLogin"

    def __init__(self, *, email: str, sent_code: "api.ayiinauth.SentCode") -> None:
        
                self.email = email  # string
        
                self.sent_code = sent_code  # auth.SentCode

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmailVerifiedLogin":
        # No flags
        
        email = String.read(b)
        
        sent_code = Object.read(b)
        
        return EmailVerifiedLogin(email=email, sent_code=sent_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.email))
        
        b.write(self.sent_code.write())
        
        return b.getvalue()