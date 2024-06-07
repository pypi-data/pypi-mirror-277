
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



class UpdateConnectedBot(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``43D8521D``

bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        recipients (:obj:`InputBusinessBotRecipients<typegram.api.ayiin.InputBusinessBotRecipients>`):
                    N/A
                
        can_reply (``bool``, *optional*):
                    N/A
                
        deleted (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["bot", "recipients", "can_reply", "deleted"]

    ID = 0x43d8521d
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, bot: "ayiin.InputUser", recipients: "ayiin.InputBusinessBotRecipients", can_reply: Optional[bool] = None, deleted: Optional[bool] = None) -> None:
        
                self.bot = bot  # InputUser
        
                self.recipients = recipients  # InputBusinessBotRecipients
        
                self.can_reply = can_reply  # true
        
                self.deleted = deleted  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateConnectedBot":
        
        flags = Int.read(b)
        
        can_reply = True if flags & (1 << 0) else False
        deleted = True if flags & (1 << 1) else False
        bot = Object.read(b)
        
        recipients = Object.read(b)
        
        return UpdateConnectedBot(bot=bot, recipients=recipients, can_reply=can_reply, deleted=deleted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(self.recipients.write())
        
        return b.getvalue()