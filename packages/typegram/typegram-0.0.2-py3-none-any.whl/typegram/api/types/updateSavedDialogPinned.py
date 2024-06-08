
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class UpdateSavedDialogPinned(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``AEAF9E74``

peer (:obj:`DialogPeer<typegram.api.ayiin.DialogPeer>`):
                    N/A
                
        pinned (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "pinned"]

    ID = 0xaeaf9e74
    QUALNAME = "types.updateSavedDialogPinned"

    def __init__(self, *, peer: "api.ayiin.DialogPeer", pinned: Optional[bool] = None) -> None:
        
                self.peer = peer  # DialogPeer
        
                self.pinned = pinned  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSavedDialogPinned":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        return UpdateSavedDialogPinned(peer=peer, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()