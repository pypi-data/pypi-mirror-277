
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



class GetRecentLocations(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``702A40E0``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        hash (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`messages.Messages<typegram.api.ayiin.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "limit", "hash"]

    ID = 0x702a40e0
    QUALNAME = "functions.functionsmessages.Messages"

    def __init__(self, *, peer: "ayiin.InputPeer", limit: int, hash: int) -> None:
        
                self.peer = peer  # InputPeer
        
                self.limit = limit  # int
        
                self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentLocations":
        # No flags
        
        peer = Object.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetRecentLocations(peer=peer, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()