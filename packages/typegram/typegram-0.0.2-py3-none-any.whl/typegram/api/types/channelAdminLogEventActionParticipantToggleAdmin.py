
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



class ChannelAdminLogEventActionParticipantToggleAdmin(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``181``
        - ID: ``D5676710``

prev_participant (:obj:`ChannelParticipant<typegram.api.ayiin.ChannelParticipant>`):
                    N/A
                
        new_participant (:obj:`ChannelParticipant<typegram.api.ayiin.ChannelParticipant>`):
                    N/A
                
    """

    __slots__: List[str] = ["prev_participant", "new_participant"]

    ID = 0xd5676710
    QUALNAME = "types.channelAdminLogEventActionParticipantToggleAdmin"

    def __init__(self, *, prev_participant: "api.ayiin.ChannelParticipant", new_participant: "api.ayiin.ChannelParticipant") -> None:
        
                self.prev_participant = prev_participant  # ChannelParticipant
        
                self.new_participant = new_participant  # ChannelParticipant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantToggleAdmin":
        # No flags
        
        prev_participant = Object.read(b)
        
        new_participant = Object.read(b)
        
        return ChannelAdminLogEventActionParticipantToggleAdmin(prev_participant=prev_participant, new_participant=new_participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_participant.write())
        
        b.write(self.new_participant.write())
        
        return b.getvalue()