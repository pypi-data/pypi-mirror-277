
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



class UpdateChatUserTyping(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``83487AF0``

chat_id (``int`` ``64-bit``):
                    N/A
                
        from_id (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        action (:obj:`SendMessageAction<typegram.api.ayiin.SendMessageAction>`):
                    N/A
                
    """

    __slots__: List[str] = ["chat_id", "from_id", "action"]

    ID = 0x83487af0
    QUALNAME = "types.updateChatUserTyping"

    def __init__(self, *, chat_id: int, from_id: "api.ayiin.Peer", action: "api.ayiin.SendMessageAction") -> None:
        
                self.chat_id = chat_id  # long
        
                self.from_id = from_id  # Peer
        
                self.action = action  # SendMessageAction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatUserTyping":
        # No flags
        
        chat_id = Long.read(b)
        
        from_id = Object.read(b)
        
        action = Object.read(b)
        
        return UpdateChatUserTyping(chat_id=chat_id, from_id=from_id, action=action)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        b.write(self.from_id.write())
        
        b.write(self.action.write())
        
        return b.getvalue()