
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



class GetPasswordSettings(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9CD4EAF9``

password (:obj:`InputCheckPasswordSRP<typegram.api.ayiin.InputCheckPasswordSRP>`):
                    N/A
                
    Returns:
        :obj:`account.PasswordSettings<typegram.api.ayiin.account.PasswordSettings>`
    """

    __slots__: List[str] = ["password"]

    ID = 0x9cd4eaf9
    QUALNAME = "functions.functionsaccount.PasswordSettings"

    def __init__(self, *, password: "ayiin.InputCheckPasswordSRP") -> None:
        
                self.password = password  # InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPasswordSettings":
        # No flags
        
        password = Object.read(b)
        
        return GetPasswordSettings(password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.password.write())
        
        return b.getvalue()