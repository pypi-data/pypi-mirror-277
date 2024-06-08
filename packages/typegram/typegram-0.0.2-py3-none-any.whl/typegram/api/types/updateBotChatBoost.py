
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



class UpdateBotChatBoost(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``904DD49C``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        boost (:obj:`Boost<typegram.api.ayiin.Boost>`):
                    N/A
                
        qts (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "boost", "qts"]

    ID = 0x904dd49c
    QUALNAME = "types.updateBotChatBoost"

    def __init__(self, *, peer: "api.ayiin.Peer", boost: "api.ayiin.Boost", qts: int) -> None:
        
                self.peer = peer  # Peer
        
                self.boost = boost  # Boost
        
                self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotChatBoost":
        # No flags
        
        peer = Object.read(b)
        
        boost = Object.read(b)
        
        qts = Int.read(b)
        
        return UpdateBotChatBoost(peer=peer, boost=boost, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.boost.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()