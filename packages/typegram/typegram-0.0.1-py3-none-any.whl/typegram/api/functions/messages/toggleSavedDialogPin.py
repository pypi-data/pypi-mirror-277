
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



class ToggleSavedDialogPin(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``AC81BBDE``

peer (:obj:`InputDialogPeer<typegram.api.ayiin.InputDialogPeer>`):
                    N/A
                
        pinned (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "pinned"]

    ID = 0xac81bbde
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputDialogPeer", pinned: Optional[bool] = None) -> None:
        
                self.peer = peer  # InputDialogPeer
        
                self.pinned = pinned  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleSavedDialogPin":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        return ToggleSavedDialogPin(peer=peer, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()