
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



class UpdatePasswordSettings(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A59B102F``

password (:obj:`InputCheckPasswordSRP<typegram.api.ayiin.InputCheckPasswordSRP>`):
                    N/A
                
        new_settings (:obj:`account.PasswordInputSettings<typegram.api.ayiin.account.PasswordInputSettings>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["password", "new_settings"]

    ID = 0xa59b102f
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, password: "ayiin.InputCheckPasswordSRP", new_settings: "ayiinaccount.PasswordInputSettings") -> None:
        
                self.password = password  # InputCheckPasswordSRP
        
                self.new_settings = new_settings  # account.PasswordInputSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePasswordSettings":
        # No flags
        
        password = Object.read(b)
        
        new_settings = Object.read(b)
        
        return UpdatePasswordSettings(password=password, new_settings=new_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.password.write())
        
        b.write(self.new_settings.write())
        
        return b.getvalue()