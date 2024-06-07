
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



class ReportReaction(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3F64C076``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        reaction_peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "id", "reaction_peer"]

    ID = 0x3f64c076
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int, reaction_peer: "ayiin.InputPeer") -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.reaction_peer = reaction_peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportReaction":
        # No flags
        
        peer = Object.read(b)
        
        id = Int.read(b)
        
        reaction_peer = Object.read(b)
        
        return ReportReaction(peer=peer, id=id, reaction_peer=reaction_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        b.write(self.reaction_peer.write())
        
        return b.getvalue()