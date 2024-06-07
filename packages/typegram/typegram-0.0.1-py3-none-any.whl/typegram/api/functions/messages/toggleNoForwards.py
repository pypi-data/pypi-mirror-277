
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



class ToggleNoForwards(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B11EAFA2``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        enabled (``bool``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "enabled"]

    ID = 0xb11eafa2
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", enabled: bool) -> None:
        
                self.peer = peer  # InputPeer
        
                self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleNoForwards":
        # No flags
        
        peer = Object.read(b)
        
        enabled = Bool.read(b)
        
        return ToggleNoForwards(peer=peer, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()