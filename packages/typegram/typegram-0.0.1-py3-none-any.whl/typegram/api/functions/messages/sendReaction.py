
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



class SendReaction(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D30D78D4``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        big (``bool``, *optional*):
                    N/A
                
        add_to_recent (``bool``, *optional*):
                    N/A
                
        reaction (List of :obj:`Reaction<typegram.api.ayiin.Reaction>`, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "big", "add_to_recent", "reaction"]

    ID = 0xd30d78d4
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", msg_id: int, big: Optional[bool] = None, add_to_recent: Optional[bool] = None, reaction: Optional[List["ayiin.Reaction"]] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.msg_id = msg_id  # int
        
                self.big = big  # true
        
                self.add_to_recent = add_to_recent  # true
        
                self.reaction = reaction  # Reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendReaction":
        
        flags = Int.read(b)
        
        big = True if flags & (1 << 1) else False
        add_to_recent = True if flags & (1 << 2) else False
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        reaction = Object.read(b) if flags & (1 << 0) else []
        
        return SendReaction(peer=peer, msg_id=msg_id, big=big, add_to_recent=add_to_recent, reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        if self.reaction is not None:
            b.write(Vector(self.reaction))
        
        return b.getvalue()