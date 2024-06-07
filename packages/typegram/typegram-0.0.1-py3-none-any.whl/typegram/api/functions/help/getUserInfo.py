
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



class GetUserInfo(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``38A08D3``

user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
    Returns:
        :obj:`help.UserInfo<typegram.api.ayiin.help.UserInfo>`
    """

    __slots__: List[str] = ["user_id"]

    ID = 0x38a08d3
    QUALNAME = "functions.functionshelp.UserInfo"

    def __init__(self, *, user_id: "ayiin.InputUser") -> None:
        
                self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUserInfo":
        # No flags
        
        user_id = Object.read(b)
        
        return GetUserInfo(user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        return b.getvalue()