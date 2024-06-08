
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



class ChannelAdminLogEventActionParticipantUnmute(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``181``
        - ID: ``E64429C0``

participant (:obj:`GroupCallParticipant<typegram.api.ayiin.GroupCallParticipant>`):
                    N/A
                
    """

    __slots__: List[str] = ["participant"]

    ID = 0xe64429c0
    QUALNAME = "types.channelAdminLogEventActionParticipantUnmute"

    def __init__(self, *, participant: "api.ayiin.GroupCallParticipant") -> None:
        
                self.participant = participant  # GroupCallParticipant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantUnmute":
        # No flags
        
        participant = Object.read(b)
        
        return ChannelAdminLogEventActionParticipantUnmute(participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.participant.write())
        
        return b.getvalue()