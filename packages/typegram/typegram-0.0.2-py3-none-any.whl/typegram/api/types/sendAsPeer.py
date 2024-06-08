
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



class SendAsPeer(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SendAsPeer`.

    Details:
        - Layer: ``181``
        - ID: ``B81C7034``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        premium_required (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "premium_required"]

    ID = 0xb81c7034
    QUALNAME = "types.sendAsPeer"

    def __init__(self, *, peer: "api.ayiin.Peer", premium_required: Optional[bool] = None) -> None:
        
                self.peer = peer  # Peer
        
                self.premium_required = premium_required  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendAsPeer":
        
        flags = Int.read(b)
        
        premium_required = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        return SendAsPeer(peer=peer, premium_required=premium_required)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()