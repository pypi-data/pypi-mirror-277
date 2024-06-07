
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



class DeleteStories(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``AE59DB5F``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (List of ``int`` ``32-bit``):
                    N/A
                
    Returns:
        List of ``int`` ``32-bit``
    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0xae59db5f
    QUALNAME = "functions.functions.Vector<int>"

    def __init__(self, *, peer: "ayiin.InputPeer", id: List[int]) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteStories":
        # No flags
        
        peer = Object.read(b)
        
        id = Object.read(b, Int)
        
        return DeleteStories(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()