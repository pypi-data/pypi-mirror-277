
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



class UnpinAllMessages(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``EE22B9A8``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        top_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.AffectedHistory<typegram.api.ayiin.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["peer", "top_msg_id"]

    ID = 0xee22b9a8
    QUALNAME = "functions.functionsmessages.AffectedHistory"

    def __init__(self, *, peer: "ayiin.InputPeer", top_msg_id: Optional[int] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UnpinAllMessages":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        return UnpinAllMessages(peer=peer, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        return b.getvalue()