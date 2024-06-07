
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



class UpdateProfilePhoto(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9E82039``

id (:obj:`InputPhoto<typegram.api.ayiin.InputPhoto>`):
                    N/A
                
        fallback (``bool``, *optional*):
                    N/A
                
        bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`, *optional*):
                    N/A
                
    Returns:
        :obj:`photos.Photo<typegram.api.ayiin.photos.Photo>`
    """

    __slots__: List[str] = ["id", "fallback", "bot"]

    ID = 0x9e82039
    QUALNAME = "functions.functionsphotos.Photo"

    def __init__(self, *, id: "ayiin.InputPhoto", fallback: Optional[bool] = None, bot: "ayiin.InputUser" = None) -> None:
        
                self.id = id  # InputPhoto
        
                self.fallback = fallback  # true
        
                self.bot = bot  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateProfilePhoto":
        
        flags = Int.read(b)
        
        fallback = True if flags & (1 << 0) else False
        bot = Object.read(b) if flags & (1 << 1) else None
        
        id = Object.read(b)
        
        return UpdateProfilePhoto(id=id, fallback=fallback, bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(self.bot.write())
        
        b.write(self.id.write())
        
        return b.getvalue()