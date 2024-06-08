
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



class TopPeerCategoryPeers(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.TopPeerCategoryPeers`.

    Details:
        - Layer: ``181``
        - ID: ``FB834291``

category (:obj:`TopPeerCategory<typegram.api.ayiin.TopPeerCategory>`):
                    N/A
                
        count (``int`` ``32-bit``):
                    N/A
                
        peers (List of :obj:`TopPeer<typegram.api.ayiin.TopPeer>`):
                    N/A
                
    """

    __slots__: List[str] = ["category", "count", "peers"]

    ID = 0xfb834291
    QUALNAME = "types.topPeerCategoryPeers"

    def __init__(self, *, category: "api.ayiin.TopPeerCategory", count: int, peers: List["api.ayiin.TopPeer"]) -> None:
        
                self.category = category  # TopPeerCategory
        
                self.count = count  # int
        
                self.peers = peers  # TopPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TopPeerCategoryPeers":
        # No flags
        
        category = Object.read(b)
        
        count = Int.read(b)
        
        peers = Object.read(b)
        
        return TopPeerCategoryPeers(category=category, count=count, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.category.write())
        
        b.write(Int(self.count))
        
        b.write(Vector(self.peers))
        
        return b.getvalue()