
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



class TogglePeerStoriesHidden(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``BD0415C4``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        hidden (``bool``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "hidden"]

    ID = 0xbd0415c4
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", hidden: bool) -> None:
        
                self.peer = peer  # InputPeer
        
                self.hidden = hidden  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TogglePeerStoriesHidden":
        # No flags
        
        peer = Object.read(b)
        
        hidden = Bool.read(b)
        
        return TogglePeerStoriesHidden(peer=peer, hidden=hidden)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bool(self.hidden))
        
        return b.getvalue()