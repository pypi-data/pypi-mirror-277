
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



class UpdateGroupCallParticipants(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``F2EBDB4E``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        participants (List of :obj:`GroupCallParticipant<typegram.api.ayiin.GroupCallParticipant>`):
                    N/A
                
        version (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["call", "participants", "version"]

    ID = 0xf2ebdb4e
    QUALNAME = "types.updateGroupCallParticipants"

    def __init__(self, *, call: "api.ayiin.InputGroupCall", participants: List["api.ayiin.GroupCallParticipant"], version: int) -> None:
        
                self.call = call  # InputGroupCall
        
                self.participants = participants  # GroupCallParticipant
        
                self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallParticipants":
        # No flags
        
        call = Object.read(b)
        
        participants = Object.read(b)
        
        version = Int.read(b)
        
        return UpdateGroupCallParticipants(call=call, participants=participants, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Vector(self.participants))
        
        b.write(Int(self.version))
        
        return b.getvalue()