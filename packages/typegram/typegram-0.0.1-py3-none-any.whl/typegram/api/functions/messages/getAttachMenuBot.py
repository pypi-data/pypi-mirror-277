
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



class GetAttachMenuBot(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``77216192``

bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
    Returns:
        :obj:`AttachMenuBotsBot<typegram.api.ayiin.AttachMenuBotsBot>`
    """

    __slots__: List[str] = ["bot"]

    ID = 0x77216192
    QUALNAME = "functions.functions.AttachMenuBotsBot"

    def __init__(self, *, bot: "ayiin.InputUser") -> None:
        
                self.bot = bot  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAttachMenuBot":
        # No flags
        
        bot = Object.read(b)
        
        return GetAttachMenuBot(bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        return b.getvalue()