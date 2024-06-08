
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



class NotifyPeer(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.NotifyPeer`.

    Details:
        - Layer: ``181``
        - ID: ``9FD40BD8``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
    """

    __slots__: List[str] = ["peer"]

    ID = 0x9fd40bd8
    QUALNAME = "types.notifyPeer"

    def __init__(self, *, peer: "api.ayiin.Peer") -> None:
        
                self.peer = peer  # Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "NotifyPeer":
        # No flags
        
        peer = Object.read(b)
        
        return NotifyPeer(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        return b.getvalue()