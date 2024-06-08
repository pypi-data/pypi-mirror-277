
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



class LoginToken(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.LoginToken`.

    Details:
        - Layer: ``181``
        - ID: ``629F1980``

expires (``int`` ``32-bit``):
                    N/A
                
        token (``bytes``):
                    N/A
                
    Functions:
        This object can be returned by 15 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            auth.exportLoginToken
            auth.importLoginToken
    """

    __slots__: List[str] = ["expires", "token"]

    ID = 0x629f1980
    QUALNAME = "types.auth.loginToken"

    def __init__(self, *, expires: int, token: bytes) -> None:
        
                self.expires = expires  # int
        
                self.token = token  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LoginToken":
        # No flags
        
        expires = Int.read(b)
        
        token = Bytes.read(b)
        
        return LoginToken(expires=expires, token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.expires))
        
        b.write(Bytes(self.token))
        
        return b.getvalue()