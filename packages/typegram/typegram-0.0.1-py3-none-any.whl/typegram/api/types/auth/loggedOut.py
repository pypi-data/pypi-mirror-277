
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



class LoggedOut(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.LoggedOut`.

    Details:
        - Layer: ``181``
        - ID: ``C3A2835F``

future_auth_token (``bytes``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            auth.SentCode
            auth.Authorization
            auth.ExportedAuthorization
            auth.LoginToken
    """

    __slots__: List[str] = ["future_auth_token"]

    ID = 0xc3a2835f
    QUALNAME = "functions.typesauth.LoggedOut"

    def __init__(self, *, future_auth_token: Optional[bytes] = None) -> None:
        
                self.future_auth_token = future_auth_token  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LoggedOut":
        
        flags = Int.read(b)
        
        future_auth_token = Bytes.read(b) if flags & (1 << 0) else None
        return LoggedOut(future_auth_token=future_auth_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.future_auth_token is not None:
            b.write(Bytes(self.future_auth_token))
        
        return b.getvalue()