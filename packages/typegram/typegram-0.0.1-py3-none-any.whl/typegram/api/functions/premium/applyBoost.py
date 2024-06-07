
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



class ApplyBoost(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``6B7DA746``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        slots (List of ``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`premium.MyBoosts<typegram.api.ayiin.premium.MyBoosts>`
    """

    __slots__: List[str] = ["peer", "slots"]

    ID = 0x6b7da746
    QUALNAME = "functions.functionspremium.MyBoosts"

    def __init__(self, *, peer: "ayiin.InputPeer", slots: Optional[List[int]] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.slots = slots  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ApplyBoost":
        
        flags = Int.read(b)
        
        slots = Object.read(b, Int) if flags & (1 << 0) else []
        
        peer = Object.read(b)
        
        return ApplyBoost(peer=peer, slots=slots)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.slots is not None:
            b.write(Vector(self.slots, Int))
        
        b.write(self.peer.write())
        
        return b.getvalue()