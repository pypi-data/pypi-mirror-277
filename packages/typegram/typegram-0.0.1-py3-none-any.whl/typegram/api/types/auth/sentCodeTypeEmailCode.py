
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



class SentCodeTypeEmailCode(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.SentCodeType`.

    Details:
        - Layer: ``181``
        - ID: ``F450F59B``

email_pattern (``str``):
                    N/A
                
        length (``int`` ``32-bit``):
                    N/A
                
        apple_signin_allowed (``bool``, *optional*):
                    N/A
                
        google_signin_allowed (``bool``, *optional*):
                    N/A
                
        reset_available_period (``int`` ``32-bit``, *optional*):
                    N/A
                
        reset_pending_date (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            auth.SentCode
            auth.Authorization
            auth.ExportedAuthorization
            auth.LoginToken
    """

    __slots__: List[str] = ["email_pattern", "length", "apple_signin_allowed", "google_signin_allowed", "reset_available_period", "reset_pending_date"]

    ID = 0xf450f59b
    QUALNAME = "functions.typesauth.SentCodeType"

    def __init__(self, *, email_pattern: str, length: int, apple_signin_allowed: Optional[bool] = None, google_signin_allowed: Optional[bool] = None, reset_available_period: Optional[int] = None, reset_pending_date: Optional[int] = None) -> None:
        
                self.email_pattern = email_pattern  # string
        
                self.length = length  # int
        
                self.apple_signin_allowed = apple_signin_allowed  # true
        
                self.google_signin_allowed = google_signin_allowed  # true
        
                self.reset_available_period = reset_available_period  # int
        
                self.reset_pending_date = reset_pending_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeEmailCode":
        
        flags = Int.read(b)
        
        apple_signin_allowed = True if flags & (1 << 0) else False
        google_signin_allowed = True if flags & (1 << 1) else False
        email_pattern = String.read(b)
        
        length = Int.read(b)
        
        reset_available_period = Int.read(b) if flags & (1 << 3) else None
        reset_pending_date = Int.read(b) if flags & (1 << 4) else None
        return SentCodeTypeEmailCode(email_pattern=email_pattern, length=length, apple_signin_allowed=apple_signin_allowed, google_signin_allowed=google_signin_allowed, reset_available_period=reset_available_period, reset_pending_date=reset_pending_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.email_pattern))
        
        b.write(Int(self.length))
        
        if self.reset_available_period is not None:
            b.write(Int(self.reset_available_period))
        
        if self.reset_pending_date is not None:
            b.write(Int(self.reset_pending_date))
        
        return b.getvalue()