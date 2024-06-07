
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



class EditFactCheck(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``589EE75``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        text (:obj:`TextWithEntities<typegram.api.ayiin.TextWithEntities>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "text"]

    ID = 0x589ee75
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", msg_id: int, text: "ayiin.TextWithEntities") -> None:
        
                self.peer = peer  # InputPeer
        
                self.msg_id = msg_id  # int
        
                self.text = text  # TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditFactCheck":
        # No flags
        
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        text = Object.read(b)
        
        return EditFactCheck(peer=peer, msg_id=msg_id, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(self.text.write())
        
        return b.getvalue()