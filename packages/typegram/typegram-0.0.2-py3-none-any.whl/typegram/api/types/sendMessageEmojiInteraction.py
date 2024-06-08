
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



class SendMessageEmojiInteraction(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SendMessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``25972BCB``

emoticon (``str``):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        interaction (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
    """

    __slots__: List[str] = ["emoticon", "msg_id", "interaction"]

    ID = 0x25972bcb
    QUALNAME = "types.sendMessageEmojiInteraction"

    def __init__(self, *, emoticon: str, msg_id: int, interaction: "api.ayiin.DataJSON") -> None:
        
                self.emoticon = emoticon  # string
        
                self.msg_id = msg_id  # int
        
                self.interaction = interaction  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageEmojiInteraction":
        # No flags
        
        emoticon = String.read(b)
        
        msg_id = Int.read(b)
        
        interaction = Object.read(b)
        
        return SendMessageEmojiInteraction(emoticon=emoticon, msg_id=msg_id, interaction=interaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.emoticon))
        
        b.write(Int(self.msg_id))
        
        b.write(self.interaction.write())
        
        return b.getvalue()