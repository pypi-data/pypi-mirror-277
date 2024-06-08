
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



class UpdatePinnedMessages(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``ED85EAB5``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        messages (List of ``int`` ``32-bit``):
                    N/A
                
        pts (``int`` ``32-bit``):
                    N/A
                
        pts_count (``int`` ``32-bit``):
                    N/A
                
        pinned (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "messages", "pts", "pts_count", "pinned"]

    ID = 0xed85eab5
    QUALNAME = "types.updatePinnedMessages"

    def __init__(self, *, peer: "api.ayiin.Peer", messages: List[int], pts: int, pts_count: int, pinned: Optional[bool] = None) -> None:
        
                self.peer = peer  # Peer
        
                self.messages = messages  # int
        
                self.pts = pts  # int
        
                self.pts_count = pts_count  # int
        
                self.pinned = pinned  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedMessages":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        messages = Object.read(b, Int)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        return UpdatePinnedMessages(peer=peer, messages=messages, pts=pts, pts_count=pts_count, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Vector(self.messages, Int))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        return b.getvalue()