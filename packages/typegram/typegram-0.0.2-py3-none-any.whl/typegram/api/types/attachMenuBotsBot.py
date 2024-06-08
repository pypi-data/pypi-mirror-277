
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class AttachMenuBotsBot(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.AttachMenuBotsBot`.

    Details:
        - Layer: ``181``
        - ID: ``93BF667F``

bot (:obj:`AttachMenuBot<typegram.api.ayiin.AttachMenuBot>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getAttachMenuBot
    """

    __slots__: List[str] = ["bot", "users"]

    ID = 0x93bf667f
    QUALNAME = "types.attachMenuBotsBot"

    def __init__(self, *, bot: "api.ayiin.AttachMenuBot", users: List["api.ayiin.User"]) -> None:
        
                self.bot = bot  # AttachMenuBot
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBotsBot":
        # No flags
        
        bot = Object.read(b)
        
        users = Object.read(b)
        
        return AttachMenuBotsBot(bot=bot, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()