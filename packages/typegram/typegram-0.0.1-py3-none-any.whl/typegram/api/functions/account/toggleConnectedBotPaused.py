
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



class ToggleConnectedBotPaused(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``646E1097``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        paused (``bool``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "paused"]

    ID = 0x646e1097
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", paused: bool) -> None:
        
                self.peer = peer  # InputPeer
        
                self.paused = paused  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleConnectedBotPaused":
        # No flags
        
        peer = Object.read(b)
        
        paused = Bool.read(b)
        
        return ToggleConnectedBotPaused(peer=peer, paused=paused)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bool(self.paused))
        
        return b.getvalue()