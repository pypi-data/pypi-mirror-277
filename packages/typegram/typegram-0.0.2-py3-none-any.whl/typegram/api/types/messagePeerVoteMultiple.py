
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



class MessagePeerVoteMultiple(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessagePeerVote`.

    Details:
        - Layer: ``181``
        - ID: ``4628F6E6``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        options (List of ``bytes``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "options", "date"]

    ID = 0x4628f6e6
    QUALNAME = "types.messagePeerVoteMultiple"

    def __init__(self, *, peer: "api.ayiin.Peer", options: List[bytes], date: int) -> None:
        
                self.peer = peer  # Peer
        
                self.options = options  # bytes
        
                self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessagePeerVoteMultiple":
        # No flags
        
        peer = Object.read(b)
        
        options = Object.read(b, Bytes)
        
        date = Int.read(b)
        
        return MessagePeerVoteMultiple(peer=peer, options=options, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.options, Bytes))
        
        b.write(Int(self.date))
        
        return b.getvalue()