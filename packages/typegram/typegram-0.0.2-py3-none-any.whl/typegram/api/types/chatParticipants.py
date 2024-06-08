
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



class ChatParticipants(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChatParticipants`.

    Details:
        - Layer: ``181``
        - ID: ``3CBC93F8``

chat_id (``int`` ``64-bit``):
                    N/A
                
        participants (List of :obj:`ChatParticipant<typegram.api.ayiin.ChatParticipant>`):
                    N/A
                
        version (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["chat_id", "participants", "version"]

    ID = 0x3cbc93f8
    QUALNAME = "types.chatParticipants"

    def __init__(self, *, chat_id: int, participants: List["api.ayiin.ChatParticipant"], version: int) -> None:
        
                self.chat_id = chat_id  # long
        
                self.participants = participants  # ChatParticipant
        
                self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipants":
        # No flags
        
        chat_id = Long.read(b)
        
        participants = Object.read(b)
        
        version = Int.read(b)
        
        return ChatParticipants(chat_id=chat_id, participants=participants, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        b.write(Vector(self.participants))
        
        b.write(Int(self.version))
        
        return b.getvalue()