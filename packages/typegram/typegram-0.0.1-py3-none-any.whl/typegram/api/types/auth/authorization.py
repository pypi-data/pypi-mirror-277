
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



class Authorization(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.Authorization`.

    Details:
        - Layer: ``181``
        - ID: ``2EA2C0D4``

user (:obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        setup_password_required (``bool``, *optional*):
                    N/A
                
        otherwise_relogin_days (``int`` ``32-bit``, *optional*):
                    N/A
                
        tmp_sessions (``int`` ``32-bit``, *optional*):
                    N/A
                
        future_auth_token (``bytes``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            auth.SentCode
            auth.Authorization
            auth.ExportedAuthorization
            auth.LoginToken
    """

    __slots__: List[str] = ["user", "setup_password_required", "otherwise_relogin_days", "tmp_sessions", "future_auth_token"]

    ID = 0x2ea2c0d4
    QUALNAME = "functions.typesauth.Authorization"

    def __init__(self, *, user: "ayiin.User", setup_password_required: Optional[bool] = None, otherwise_relogin_days: Optional[int] = None, tmp_sessions: Optional[int] = None, future_auth_token: Optional[bytes] = None) -> None:
        
                self.user = user  # User
        
                self.setup_password_required = setup_password_required  # true
        
                self.otherwise_relogin_days = otherwise_relogin_days  # int
        
                self.tmp_sessions = tmp_sessions  # int
        
                self.future_auth_token = future_auth_token  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Authorization":
        
        flags = Int.read(b)
        
        setup_password_required = True if flags & (1 << 1) else False
        otherwise_relogin_days = Int.read(b) if flags & (1 << 1) else None
        tmp_sessions = Int.read(b) if flags & (1 << 0) else None
        future_auth_token = Bytes.read(b) if flags & (1 << 2) else None
        user = Object.read(b)
        
        return Authorization(user=user, setup_password_required=setup_password_required, otherwise_relogin_days=otherwise_relogin_days, tmp_sessions=tmp_sessions, future_auth_token=future_auth_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.otherwise_relogin_days is not None:
            b.write(Int(self.otherwise_relogin_days))
        
        if self.tmp_sessions is not None:
            b.write(Int(self.tmp_sessions))
        
        if self.future_auth_token is not None:
            b.write(Bytes(self.future_auth_token))
        
        b.write(self.user.write())
        
        return b.getvalue()