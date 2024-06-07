
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



class LaunchPrepaidGiveaway(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``5FF58F20``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        giveaway_id (``int`` ``64-bit``):
                    N/A
                
        purpose (:obj:`InputStorePaymentPurpose<typegram.api.ayiin.InputStorePaymentPurpose>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "giveaway_id", "purpose"]

    ID = 0x5ff58f20
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", giveaway_id: int, purpose: "ayiin.InputStorePaymentPurpose") -> None:
        
                self.peer = peer  # InputPeer
        
                self.giveaway_id = giveaway_id  # long
        
                self.purpose = purpose  # InputStorePaymentPurpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LaunchPrepaidGiveaway":
        # No flags
        
        peer = Object.read(b)
        
        giveaway_id = Long.read(b)
        
        purpose = Object.read(b)
        
        return LaunchPrepaidGiveaway(peer=peer, giveaway_id=giveaway_id, purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.giveaway_id))
        
        b.write(self.purpose.write())
        
        return b.getvalue()