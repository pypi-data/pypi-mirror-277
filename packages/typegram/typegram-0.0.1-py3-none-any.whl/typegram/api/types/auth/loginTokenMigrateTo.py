
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



class LoginTokenMigrateTo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.LoginToken`.

    Details:
        - Layer: ``181``
        - ID: ``68E9916``

dc_id (``int`` ``32-bit``):
                    N/A
                
        token (``bytes``):
                    N/A
                
    Functions:
        This object can be returned by 15 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            auth.SentCode
            auth.Authorization
            auth.ExportedAuthorization
            auth.LoginToken
    """

    __slots__: List[str] = ["dc_id", "token"]

    ID = 0x68e9916
    QUALNAME = "functions.typesauth.LoginToken"

    def __init__(self, *, dc_id: int, token: bytes) -> None:
        
                self.dc_id = dc_id  # int
        
                self.token = token  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LoginTokenMigrateTo":
        # No flags
        
        dc_id = Int.read(b)
        
        token = Bytes.read(b)
        
        return LoginTokenMigrateTo(dc_id=dc_id, token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.dc_id))
        
        b.write(Bytes(self.token))
        
        return b.getvalue()