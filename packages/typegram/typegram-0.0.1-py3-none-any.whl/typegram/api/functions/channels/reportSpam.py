
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



class ReportSpam(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F44A8315``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        participant (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (List of ``int`` ``32-bit``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "participant", "id"]

    ID = 0xf44a8315
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, channel: "ayiin.InputChannel", participant: "ayiin.InputPeer", id: List[int]) -> None:
        
                self.channel = channel  # InputChannel
        
                self.participant = participant  # InputPeer
        
                self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportSpam":
        # No flags
        
        channel = Object.read(b)
        
        participant = Object.read(b)
        
        id = Object.read(b, Int)
        
        return ReportSpam(channel=channel, participant=participant, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.participant.write())
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()