
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



class GetBotInfo(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``DCD914FD``

lang_code (``str``):
                    N/A
                
        bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`, *optional*):
                    N/A
                
    Returns:
        :obj:`bots.BotInfo<typegram.api.ayiin.bots.BotInfo>`
    """

    __slots__: List[str] = ["lang_code", "bot"]

    ID = 0xdcd914fd
    QUALNAME = "functions.functionsbots.BotInfo"

    def __init__(self, *, lang_code: str, bot: "ayiin.InputUser" = None) -> None:
        
                self.lang_code = lang_code  # string
        
                self.bot = bot  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotInfo":
        
        flags = Int.read(b)
        
        bot = Object.read(b) if flags & (1 << 0) else None
        
        lang_code = String.read(b)
        
        return GetBotInfo(lang_code=lang_code, bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(self.bot.write())
        
        b.write(String(self.lang_code))
        
        return b.getvalue()