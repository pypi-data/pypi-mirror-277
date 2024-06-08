
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



class UpdatePendingJoinRequests(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``7063C3DB``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        requests_pending (``int`` ``32-bit``):
                    N/A
                
        recent_requesters (List of ``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "requests_pending", "recent_requesters"]

    ID = 0x7063c3db
    QUALNAME = "types.updatePendingJoinRequests"

    def __init__(self, *, peer: "api.ayiin.Peer", requests_pending: int, recent_requesters: List[int]) -> None:
        
                self.peer = peer  # Peer
        
                self.requests_pending = requests_pending  # int
        
                self.recent_requesters = recent_requesters  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePendingJoinRequests":
        # No flags
        
        peer = Object.read(b)
        
        requests_pending = Int.read(b)
        
        recent_requesters = Object.read(b, Long)
        
        return UpdatePendingJoinRequests(peer=peer, requests_pending=requests_pending, recent_requesters=recent_requesters)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.requests_pending))
        
        b.write(Vector(self.recent_requesters, Long))
        
        return b.getvalue()