
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



class SentCodeTypeSetUpEmailRequired(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.SentCodeType`.

    Details:
        - Layer: ``181``
        - ID: ``A5491DEA``

apple_signin_allowed (``bool``, *optional*):
                    N/A
                
        google_signin_allowed (``bool``, *optional*):
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

    __slots__: List[str] = ["apple_signin_allowed", "google_signin_allowed"]

    ID = 0xa5491dea
    QUALNAME = "functions.typesauth.SentCodeType"

    def __init__(self, *, apple_signin_allowed: Optional[bool] = None, google_signin_allowed: Optional[bool] = None) -> None:
        
                self.apple_signin_allowed = apple_signin_allowed  # true
        
                self.google_signin_allowed = google_signin_allowed  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeSetUpEmailRequired":
        
        flags = Int.read(b)
        
        apple_signin_allowed = True if flags & (1 << 0) else False
        google_signin_allowed = True if flags & (1 << 1) else False
        return SentCodeTypeSetUpEmailRequired(apple_signin_allowed=apple_signin_allowed, google_signin_allowed=google_signin_allowed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()