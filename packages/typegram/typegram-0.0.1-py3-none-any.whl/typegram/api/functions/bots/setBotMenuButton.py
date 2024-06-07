
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



class SetBotMenuButton(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``4504D54F``

user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        button (:obj:`BotMenuButton<typegram.api.ayiin.BotMenuButton>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["user_id", "button"]

    ID = 0x4504d54f
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, user_id: "ayiin.InputUser", button: "ayiin.BotMenuButton") -> None:
        
                self.user_id = user_id  # InputUser
        
                self.button = button  # BotMenuButton

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotMenuButton":
        # No flags
        
        user_id = Object.read(b)
        
        button = Object.read(b)
        
        return SetBotMenuButton(user_id=user_id, button=button)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(self.button.write())
        
        return b.getvalue()