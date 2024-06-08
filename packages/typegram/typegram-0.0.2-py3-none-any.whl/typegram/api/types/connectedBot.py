
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



class ConnectedBot(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ConnectedBot`.

    Details:
        - Layer: ``181``
        - ID: ``BD068601``

bot_id (``int`` ``64-bit``):
                    N/A
                
        recipients (:obj:`BusinessBotRecipients<typegram.api.ayiin.BusinessBotRecipients>`):
                    N/A
                
        can_reply (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["bot_id", "recipients", "can_reply"]

    ID = 0xbd068601
    QUALNAME = "types.connectedBot"

    def __init__(self, *, bot_id: int, recipients: "api.ayiin.BusinessBotRecipients", can_reply: Optional[bool] = None) -> None:
        
                self.bot_id = bot_id  # long
        
                self.recipients = recipients  # BusinessBotRecipients
        
                self.can_reply = can_reply  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConnectedBot":
        
        flags = Int.read(b)
        
        can_reply = True if flags & (1 << 0) else False
        bot_id = Long.read(b)
        
        recipients = Object.read(b)
        
        return ConnectedBot(bot_id=bot_id, recipients=recipients, can_reply=can_reply)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.bot_id))
        
        b.write(self.recipients.write())
        
        return b.getvalue()