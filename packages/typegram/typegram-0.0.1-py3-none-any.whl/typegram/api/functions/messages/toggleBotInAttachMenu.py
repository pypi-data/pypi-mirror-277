
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



class ToggleBotInAttachMenu(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``69F59D69``

bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        enabled (``bool``):
                    N/A
                
        write_allowed (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["bot", "enabled", "write_allowed"]

    ID = 0x69f59d69
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, bot: "ayiin.InputUser", enabled: bool, write_allowed: Optional[bool] = None) -> None:
        
                self.bot = bot  # InputUser
        
                self.enabled = enabled  # Bool
        
                self.write_allowed = write_allowed  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleBotInAttachMenu":
        
        flags = Int.read(b)
        
        write_allowed = True if flags & (1 << 0) else False
        bot = Object.read(b)
        
        enabled = Bool.read(b)
        
        return ToggleBotInAttachMenu(bot=bot, enabled=enabled, write_allowed=write_allowed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()