
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



class GetParticipant(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A0AB6CC6``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        participant (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
    Returns:
        :obj:`channels.ChannelParticipant<typegram.api.ayiin.channels.ChannelParticipant>`
    """

    __slots__: List[str] = ["channel", "participant"]

    ID = 0xa0ab6cc6
    QUALNAME = "functions.channels.getParticipant"

    def __init__(self, *, channel: "api.ayiin.InputChannel", participant: "api.ayiin.InputPeer") -> None:
        
                self.channel = channel  # InputChannel
        
                self.participant = participant  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetParticipant":
        # No flags
        
        channel = Object.read(b)
        
        participant = Object.read(b)
        
        return GetParticipant(channel=channel, participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.participant.write())
        
        return b.getvalue()