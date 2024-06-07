
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



class SendBotRequestedPeer(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``91B2D060``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        button_id (``int`` ``32-bit``):
                    N/A
                
        requested_peers (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "button_id", "requested_peers"]

    ID = 0x91b2d060
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", msg_id: int, button_id: int, requested_peers: List["ayiin.InputPeer"]) -> None:
        
                self.peer = peer  # InputPeer
        
                self.msg_id = msg_id  # int
        
                self.button_id = button_id  # int
        
                self.requested_peers = requested_peers  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendBotRequestedPeer":
        # No flags
        
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        button_id = Int.read(b)
        
        requested_peers = Object.read(b)
        
        return SendBotRequestedPeer(peer=peer, msg_id=msg_id, button_id=button_id, requested_peers=requested_peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.button_id))
        
        b.write(Vector(self.requested_peers))
        
        return b.getvalue()