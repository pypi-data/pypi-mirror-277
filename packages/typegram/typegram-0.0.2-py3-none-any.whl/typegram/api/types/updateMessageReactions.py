
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



class UpdateMessageReactions(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``5E1B3CB8``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        reactions (:obj:`MessageReactions<typegram.api.ayiin.MessageReactions>`):
                    N/A
                
        top_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "msg_id", "reactions", "top_msg_id"]

    ID = 0x5e1b3cb8
    QUALNAME = "types.updateMessageReactions"

    def __init__(self, *, peer: "api.ayiin.Peer", msg_id: int, reactions: "api.ayiin.MessageReactions", top_msg_id: Optional[int] = None) -> None:
        
                self.peer = peer  # Peer
        
                self.msg_id = msg_id  # int
        
                self.reactions = reactions  # MessageReactions
        
                self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessageReactions":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        reactions = Object.read(b)
        
        return UpdateMessageReactions(peer=peer, msg_id=msg_id, reactions=reactions, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(self.reactions.write())
        
        return b.getvalue()