
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



class InvokeWebViewCustomMethod(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``87FC5E7``

bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        custom_method (``str``):
                    N/A
                
        params (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
    Returns:
        :obj:`DataJSON<typegram.api.ayiin.DataJSON>`
    """

    __slots__: List[str] = ["bot", "custom_method", "params"]

    ID = 0x87fc5e7
    QUALNAME = "functions.functions.DataJSON"

    def __init__(self, *, bot: "ayiin.InputUser", custom_method: str, params: "ayiin.DataJSON") -> None:
        
                self.bot = bot  # InputUser
        
                self.custom_method = custom_method  # string
        
                self.params = params  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWebViewCustomMethod":
        # No flags
        
        bot = Object.read(b)
        
        custom_method = String.read(b)
        
        params = Object.read(b)
        
        return InvokeWebViewCustomMethod(bot=bot, custom_method=custom_method, params=params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(String(self.custom_method))
        
        b.write(self.params.write())
        
        return b.getvalue()