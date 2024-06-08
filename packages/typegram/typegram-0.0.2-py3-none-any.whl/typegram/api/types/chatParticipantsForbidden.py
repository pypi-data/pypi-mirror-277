
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



class ChatParticipantsForbidden(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChatParticipants`.

    Details:
        - Layer: ``181``
        - ID: ``8763D3E1``

chat_id (``int`` ``64-bit``):
                    N/A
                
        is_self_participant (:obj:`ChatParticipant<typegram.api.ayiin.ChatParticipant>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["chat_id", "is_self_participant"]

    ID = 0x8763d3e1
    QUALNAME = "types.chatParticipantsForbidden"

    def __init__(self, *, chat_id: int, is_self_participant: "api.ayiin.ChatParticipant" = None) -> None:
        
                self.chat_id = chat_id  # long
        
                self.is_self_participant = is_self_participant  # ChatParticipant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipantsForbidden":
        
        flags = Int.read(b)
        
        chat_id = Long.read(b)
        
        is_self_participant = Object.read(b) if flags & (1 << 0) else None
        
        return ChatParticipantsForbidden(chat_id=chat_id, is_self_participant=is_self_participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.chat_id))
        
        if self.is_self_participant is not None:
            b.write(self.is_self_participant.write())
        
        return b.getvalue()