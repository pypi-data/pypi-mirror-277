
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



class MessageActionGeoProximityReached(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``98E0D697``

from_id (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        to_id (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        distance (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["from_id", "to_id", "distance"]

    ID = 0x98e0d697
    QUALNAME = "types.messageActionGeoProximityReached"

    def __init__(self, *, from_id: "api.ayiin.Peer", to_id: "api.ayiin.Peer", distance: int) -> None:
        
                self.from_id = from_id  # Peer
        
                self.to_id = to_id  # Peer
        
                self.distance = distance  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGeoProximityReached":
        # No flags
        
        from_id = Object.read(b)
        
        to_id = Object.read(b)
        
        distance = Int.read(b)
        
        return MessageActionGeoProximityReached(from_id=from_id, to_id=to_id, distance=distance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.from_id.write())
        
        b.write(self.to_id.write())
        
        b.write(Int(self.distance))
        
        return b.getvalue()