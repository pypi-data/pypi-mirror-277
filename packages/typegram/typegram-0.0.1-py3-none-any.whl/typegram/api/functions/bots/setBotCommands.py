
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



class SetBotCommands(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``517165A``

scope (:obj:`BotCommandScope<typegram.api.ayiin.BotCommandScope>`):
                    N/A
                
        lang_code (``str``):
                    N/A
                
        commands (List of :obj:`BotCommand<typegram.api.ayiin.BotCommand>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["scope", "lang_code", "commands"]

    ID = 0x517165a
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, scope: "ayiin.BotCommandScope", lang_code: str, commands: List["ayiin.BotCommand"]) -> None:
        
                self.scope = scope  # BotCommandScope
        
                self.lang_code = lang_code  # string
        
                self.commands = commands  # BotCommand

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotCommands":
        # No flags
        
        scope = Object.read(b)
        
        lang_code = String.read(b)
        
        commands = Object.read(b)
        
        return SetBotCommands(scope=scope, lang_code=lang_code, commands=commands)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.scope.write())
        
        b.write(String(self.lang_code))
        
        b.write(Vector(self.commands))
        
        return b.getvalue()