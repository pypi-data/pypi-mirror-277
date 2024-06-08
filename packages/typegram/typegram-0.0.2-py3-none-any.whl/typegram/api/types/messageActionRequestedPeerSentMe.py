
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



class MessageActionRequestedPeerSentMe(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``93B31848``

button_id (``int`` ``32-bit``):
                    N/A
                
        peers (List of :obj:`RequestedPeer<typegram.api.ayiin.RequestedPeer>`):
                    N/A
                
    """

    __slots__: List[str] = ["button_id", "peers"]

    ID = 0x93b31848
    QUALNAME = "types.messageActionRequestedPeerSentMe"

    def __init__(self, *, button_id: int, peers: List["api.ayiin.RequestedPeer"]) -> None:
        
                self.button_id = button_id  # int
        
                self.peers = peers  # RequestedPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionRequestedPeerSentMe":
        # No flags
        
        button_id = Int.read(b)
        
        peers = Object.read(b)
        
        return MessageActionRequestedPeerSentMe(button_id=button_id, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.button_id))
        
        b.write(Vector(self.peers))
        
        return b.getvalue()