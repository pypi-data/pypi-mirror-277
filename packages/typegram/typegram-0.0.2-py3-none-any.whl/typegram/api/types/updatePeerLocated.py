
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



class UpdatePeerLocated(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``B4AFCFB0``

peers (List of :obj:`PeerLocated<typegram.api.ayiin.PeerLocated>`):
                    N/A
                
    """

    __slots__: List[str] = ["peers"]

    ID = 0xb4afcfb0
    QUALNAME = "types.updatePeerLocated"

    def __init__(self, *, peers: List["api.ayiin.PeerLocated"]) -> None:
        
                self.peers = peers  # PeerLocated

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePeerLocated":
        # No flags
        
        peers = Object.read(b)
        
        return UpdatePeerLocated(peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.peers))
        
        return b.getvalue()