
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



class CheckPassword(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D18B4D16``

password (:obj:`InputCheckPasswordSRP<typegram.api.ayiin.InputCheckPasswordSRP>`):
                    N/A
                
    Returns:
        :obj:`auth.Authorization<typegram.api.ayiin.auth.Authorization>`
    """

    __slots__: List[str] = ["password"]

    ID = 0xd18b4d16
    QUALNAME = "functions.functionsauth.Authorization"

    def __init__(self, *, password: "ayiin.InputCheckPasswordSRP") -> None:
        
                self.password = password  # InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckPassword":
        # No flags
        
        password = Object.read(b)
        
        return CheckPassword(password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.password.write())
        
        return b.getvalue()