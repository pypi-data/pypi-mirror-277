
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



class JoinChatlistInvite(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A6B1E39A``

slug (``str``):
                    N/A
                
        peers (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["slug", "peers"]

    ID = 0xa6b1e39a
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, slug: str, peers: List["ayiin.InputPeer"]) -> None:
        
                self.slug = slug  # string
        
                self.peers = peers  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JoinChatlistInvite":
        # No flags
        
        slug = String.read(b)
        
        peers = Object.read(b)
        
        return JoinChatlistInvite(slug=slug, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.slug))
        
        b.write(Vector(self.peers))
        
        return b.getvalue()