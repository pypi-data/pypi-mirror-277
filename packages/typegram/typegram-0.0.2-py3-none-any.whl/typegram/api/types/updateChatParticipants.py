
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



class UpdateChatParticipants(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``7761198``

participants (:obj:`ChatParticipants<typegram.api.ayiin.ChatParticipants>`):
                    N/A
                
    """

    __slots__: List[str] = ["participants"]

    ID = 0x7761198
    QUALNAME = "types.updateChatParticipants"

    def __init__(self, *, participants: "api.ayiin.ChatParticipants") -> None:
        
                self.participants = participants  # ChatParticipants

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatParticipants":
        # No flags
        
        participants = Object.read(b)
        
        return UpdateChatParticipants(participants=participants)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.participants.write())
        
        return b.getvalue()