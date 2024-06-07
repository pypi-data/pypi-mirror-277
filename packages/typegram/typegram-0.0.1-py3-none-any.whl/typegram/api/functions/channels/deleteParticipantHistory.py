
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

from typegram.api import ayiin, functions
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class DeleteParticipantHistory(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``367544DB``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        participant (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
    Returns:
        :obj:`messages.AffectedHistory<typegram.api.ayiin.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["channel", "participant"]

    ID = 0x367544db
    QUALNAME = "functions.functionsmessages.AffectedHistory"

    def __init__(self, *, channel: "ayiin.InputChannel", participant: "ayiin.InputPeer") -> None:
        
                self.channel = channel  # InputChannel
        
                self.participant = participant  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteParticipantHistory":
        # No flags
        
        channel = Object.read(b)
        
        participant = Object.read(b)
        
        return DeleteParticipantHistory(channel=channel, participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.participant.write())
        
        return b.getvalue()