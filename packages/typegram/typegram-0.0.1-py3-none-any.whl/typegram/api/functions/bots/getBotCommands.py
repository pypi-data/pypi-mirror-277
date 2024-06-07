
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



class GetBotCommands(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E34C0DD6``

scope (:obj:`BotCommandScope<typegram.api.ayiin.BotCommandScope>`):
                    N/A
                
        lang_code (``str``):
                    N/A
                
    Returns:
        List of :obj:`BotCommand<typegram.api.ayiin.BotCommand>`
    """

    __slots__: List[str] = ["scope", "lang_code"]

    ID = 0xe34c0dd6
    QUALNAME = "functions.functions.Vector<BotCommand>"

    def __init__(self, *, scope: "ayiin.BotCommandScope", lang_code: str) -> None:
        
                self.scope = scope  # BotCommandScope
        
                self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotCommands":
        # No flags
        
        scope = Object.read(b)
        
        lang_code = String.read(b)
        
        return GetBotCommands(scope=scope, lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.scope.write())
        
        b.write(String(self.lang_code))
        
        return b.getvalue()