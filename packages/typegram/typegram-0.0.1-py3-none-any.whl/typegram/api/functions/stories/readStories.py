
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



class ReadStories(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A556DAC8``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        max_id (``int`` ``32-bit``):
                    N/A
                
    Returns:
        List of ``int`` ``32-bit``
    """

    __slots__: List[str] = ["peer", "max_id"]

    ID = 0xa556dac8
    QUALNAME = "functions.functions.Vector<int>"

    def __init__(self, *, peer: "ayiin.InputPeer", max_id: int) -> None:
        
                self.peer = peer  # InputPeer
        
                self.max_id = max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadStories":
        # No flags
        
        peer = Object.read(b)
        
        max_id = Int.read(b)
        
        return ReadStories(peer=peer, max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.max_id))
        
        return b.getvalue()