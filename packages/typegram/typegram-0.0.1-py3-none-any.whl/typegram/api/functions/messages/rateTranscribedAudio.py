
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



class RateTranscribedAudio(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``7F1D072F``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        transcription_id (``int`` ``64-bit``):
                    N/A
                
        good (``bool``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "msg_id", "transcription_id", "good"]

    ID = 0x7f1d072f
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", msg_id: int, transcription_id: int, good: bool) -> None:
        
                self.peer = peer  # InputPeer
        
                self.msg_id = msg_id  # int
        
                self.transcription_id = transcription_id  # long
        
                self.good = good  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RateTranscribedAudio":
        # No flags
        
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        transcription_id = Long.read(b)
        
        good = Bool.read(b)
        
        return RateTranscribedAudio(peer=peer, msg_id=msg_id, transcription_id=transcription_id, good=good)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.transcription_id))
        
        b.write(Bool(self.good))
        
        return b.getvalue()