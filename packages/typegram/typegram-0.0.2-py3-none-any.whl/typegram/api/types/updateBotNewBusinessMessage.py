
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



class UpdateBotNewBusinessMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``9DDB347C``

connection_id (``str``):
                    N/A
                
        message (:obj:`Message<typegram.api.ayiin.Message>`):
                    N/A
                
        qts (``int`` ``32-bit``):
                    N/A
                
        reply_to_message (:obj:`Message<typegram.api.ayiin.Message>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["connection_id", "message", "qts", "reply_to_message"]

    ID = 0x9ddb347c
    QUALNAME = "types.updateBotNewBusinessMessage"

    def __init__(self, *, connection_id: str, message: "api.ayiin.Message", qts: int, reply_to_message: "api.ayiin.Message" = None) -> None:
        
                self.connection_id = connection_id  # string
        
                self.message = message  # Message
        
                self.qts = qts  # int
        
                self.reply_to_message = reply_to_message  # Message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotNewBusinessMessage":
        
        flags = Int.read(b)
        
        connection_id = String.read(b)
        
        message = Object.read(b)
        
        reply_to_message = Object.read(b) if flags & (1 << 0) else None
        
        qts = Int.read(b)
        
        return UpdateBotNewBusinessMessage(connection_id=connection_id, message=message, qts=qts, reply_to_message=reply_to_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.connection_id))
        
        b.write(self.message.write())
        
        if self.reply_to_message is not None:
            b.write(self.reply_to_message.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()