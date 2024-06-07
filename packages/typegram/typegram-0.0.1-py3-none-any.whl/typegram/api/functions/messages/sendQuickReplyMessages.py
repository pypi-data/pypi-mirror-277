
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



class SendQuickReplyMessages(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``6C750DE1``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        shortcut_id (``int`` ``32-bit``):
                    N/A
                
        id (List of ``int`` ``32-bit``):
                    N/A
                
        random_id (List of ``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "shortcut_id", "id", "random_id"]

    ID = 0x6c750de1
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", shortcut_id: int, id: List[int], random_id: List[int]) -> None:
        
                self.peer = peer  # InputPeer
        
                self.shortcut_id = shortcut_id  # int
        
                self.id = id  # int
        
                self.random_id = random_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendQuickReplyMessages":
        # No flags
        
        peer = Object.read(b)
        
        shortcut_id = Int.read(b)
        
        id = Object.read(b, Int)
        
        random_id = Object.read(b, Long)
        
        return SendQuickReplyMessages(peer=peer, shortcut_id=shortcut_id, id=id, random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.shortcut_id))
        
        b.write(Vector(self.id, Int))
        
        b.write(Vector(self.random_id, Long))
        
        return b.getvalue()