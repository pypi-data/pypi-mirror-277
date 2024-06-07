
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



class GetSavedReactionTags(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3637E05B``

hash (``int`` ``64-bit``):
                    N/A
                
        peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.SavedReactionTags<typegram.api.ayiin.messages.SavedReactionTags>`
    """

    __slots__: List[str] = ["hash", "peer"]

    ID = 0x3637e05b
    QUALNAME = "functions.functionsmessages.SavedReactionTags"

    def __init__(self, *, hash: int, peer: "ayiin.InputPeer" = None) -> None:
        
                self.hash = hash  # long
        
                self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedReactionTags":
        
        flags = Int.read(b)
        
        peer = Object.read(b) if flags & (1 << 0) else None
        
        hash = Long.read(b)
        
        return GetSavedReactionTags(hash=hash, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(Long(self.hash))
        
        return b.getvalue()