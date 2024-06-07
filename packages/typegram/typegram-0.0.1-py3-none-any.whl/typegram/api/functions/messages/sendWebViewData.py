
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



class SendWebViewData(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``DC0242C8``

bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        random_id (``int`` ``64-bit``):
                    N/A
                
        button_text (``str``):
                    N/A
                
        data (``str``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["bot", "random_id", "button_text", "data"]

    ID = 0xdc0242c8
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, bot: "ayiin.InputUser", random_id: int, button_text: str, data: str) -> None:
        
                self.bot = bot  # InputUser
        
                self.random_id = random_id  # long
        
                self.button_text = button_text  # string
        
                self.data = data  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendWebViewData":
        # No flags
        
        bot = Object.read(b)
        
        random_id = Long.read(b)
        
        button_text = String.read(b)
        
        data = String.read(b)
        
        return SendWebViewData(bot=bot, random_id=random_id, button_text=button_text, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(Long(self.random_id))
        
        b.write(String(self.button_text))
        
        b.write(String(self.data))
        
        return b.getvalue()