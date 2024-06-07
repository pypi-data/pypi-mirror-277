
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



class GetFactCheck(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B9CDC5EE``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        msg_id (List of ``int`` ``32-bit``):
                    N/A
                
    Returns:
        List of :obj:`FactCheck<typegram.api.ayiin.FactCheck>`
    """

    __slots__: List[str] = ["peer", "msg_id"]

    ID = 0xb9cdc5ee
    QUALNAME = "functions.functions.Vector<FactCheck>"

    def __init__(self, *, peer: "ayiin.InputPeer", msg_id: List[int]) -> None:
        
                self.peer = peer  # InputPeer
        
                self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFactCheck":
        # No flags
        
        peer = Object.read(b)
        
        msg_id = Object.read(b, Int)
        
        return GetFactCheck(peer=peer, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.msg_id, Int))
        
        return b.getvalue()