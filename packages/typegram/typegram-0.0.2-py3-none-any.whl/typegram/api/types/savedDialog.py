
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



class SavedDialog(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SavedDialog`.

    Details:
        - Layer: ``181``
        - ID: ``BD87CB6C``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        top_message (``int`` ``32-bit``):
                    N/A
                
        pinned (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "top_message", "pinned"]

    ID = 0xbd87cb6c
    QUALNAME = "types.savedDialog"

    def __init__(self, *, peer: "api.ayiin.Peer", top_message: int, pinned: Optional[bool] = None) -> None:
        
                self.peer = peer  # Peer
        
                self.top_message = top_message  # int
        
                self.pinned = pinned  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedDialog":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        peer = Object.read(b)
        
        top_message = Int.read(b)
        
        return SavedDialog(peer=peer, top_message=top_message, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_message))
        
        return b.getvalue()