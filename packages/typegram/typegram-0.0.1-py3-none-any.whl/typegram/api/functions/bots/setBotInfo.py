
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



class SetBotInfo(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``10CF3123``

lang_code (``str``):
                    N/A
                
        bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`, *optional*):
                    N/A
                
        name (``str``, *optional*):
                    N/A
                
        about (``str``, *optional*):
                    N/A
                
        description (``str``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["lang_code", "bot", "name", "about", "description"]

    ID = 0x10cf3123
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, lang_code: str, bot: "ayiin.InputUser" = None, name: Optional[str] = None, about: Optional[str] = None, description: Optional[str] = None) -> None:
        
                self.lang_code = lang_code  # string
        
                self.bot = bot  # InputUser
        
                self.name = name  # string
        
                self.about = about  # string
        
                self.description = description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotInfo":
        
        flags = Int.read(b)
        
        bot = Object.read(b) if flags & (1 << 2) else None
        
        lang_code = String.read(b)
        
        name = String.read(b) if flags & (1 << 3) else None
        about = String.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        return SetBotInfo(lang_code=lang_code, bot=bot, name=name, about=about, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(self.bot.write())
        
        b.write(String(self.lang_code))
        
        if self.name is not None:
            b.write(String(self.name))
        
        if self.about is not None:
            b.write(String(self.about))
        
        if self.description is not None:
            b.write(String(self.description))
        
        return b.getvalue()