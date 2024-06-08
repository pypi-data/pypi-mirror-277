
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



class UpdateTranscribedAudio(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``84CD5A``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        transcription_id (``int`` ``64-bit``):
                    N/A
                
        text (``str``):
                    N/A
                
        pending (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "msg_id", "transcription_id", "text", "pending"]

    ID = 0x84cd5a
    QUALNAME = "types.updateTranscribedAudio"

    def __init__(self, *, peer: "api.ayiin.Peer", msg_id: int, transcription_id: int, text: str, pending: Optional[bool] = None) -> None:
        
                self.peer = peer  # Peer
        
                self.msg_id = msg_id  # int
        
                self.transcription_id = transcription_id  # long
        
                self.text = text  # string
        
                self.pending = pending  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateTranscribedAudio":
        
        flags = Int.read(b)
        
        pending = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        transcription_id = Long.read(b)
        
        text = String.read(b)
        
        return UpdateTranscribedAudio(peer=peer, msg_id=msg_id, transcription_id=transcription_id, text=text, pending=pending)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.transcription_id))
        
        b.write(String(self.text))
        
        return b.getvalue()