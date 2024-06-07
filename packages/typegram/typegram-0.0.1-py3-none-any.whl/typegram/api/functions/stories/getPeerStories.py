
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



class GetPeerStories(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``2C4ADA50``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
    Returns:
        :obj:`stories.PeerStories<typegram.api.ayiin.stories.PeerStories>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0x2c4ada50
    QUALNAME = "functions.functionsstories.PeerStories"

    def __init__(self, *, peer: "ayiin.InputPeer") -> None:
        
                self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerStories":
        # No flags
        
        peer = Object.read(b)
        
        return GetPeerStories(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        return b.getvalue()