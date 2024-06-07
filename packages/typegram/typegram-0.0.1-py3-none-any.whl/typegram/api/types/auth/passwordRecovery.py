
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



class PasswordRecovery(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.PasswordRecovery`.

    Details:
        - Layer: ``181``
        - ID: ``137948A5``

email_pattern (``str``):
                    N/A
                
    Functions:
        This object can be returned by 21 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            auth.SentCode
            auth.Authorization
            auth.ExportedAuthorization
            auth.LoginToken
    """

    __slots__: List[str] = ["email_pattern"]

    ID = 0x137948a5
    QUALNAME = "functions.typesauth.PasswordRecovery"

    def __init__(self, *, email_pattern: str) -> None:
        
                self.email_pattern = email_pattern  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasswordRecovery":
        # No flags
        
        email_pattern = String.read(b)
        
        return PasswordRecovery(email_pattern=email_pattern)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.email_pattern))
        
        return b.getvalue()