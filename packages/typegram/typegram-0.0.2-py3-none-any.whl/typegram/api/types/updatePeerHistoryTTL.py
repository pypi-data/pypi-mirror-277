
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



class UpdatePeerHistoryTTL(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``BB9BB9A5``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        ttl_period (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "ttl_period"]

    ID = 0xbb9bb9a5
    QUALNAME = "types.updatePeerHistoryTTL"

    def __init__(self, *, peer: "api.ayiin.Peer", ttl_period: Optional[int] = None) -> None:
        
                self.peer = peer  # Peer
        
                self.ttl_period = ttl_period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePeerHistoryTTL":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        ttl_period = Int.read(b) if flags & (1 << 0) else None
        return UpdatePeerHistoryTTL(peer=peer, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()