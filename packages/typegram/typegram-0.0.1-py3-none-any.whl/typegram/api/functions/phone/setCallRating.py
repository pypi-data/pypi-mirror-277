
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



class SetCallRating(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``59EAD627``

peer (:obj:`InputPhoneCall<typegram.api.ayiin.InputPhoneCall>`):
                    N/A
                
        rating (``int`` ``32-bit``):
                    N/A
                
        comment (``str``):
                    N/A
                
        user_initiative (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "rating", "comment", "user_initiative"]

    ID = 0x59ead627
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPhoneCall", rating: int, comment: str, user_initiative: Optional[bool] = None) -> None:
        
                self.peer = peer  # InputPhoneCall
        
                self.rating = rating  # int
        
                self.comment = comment  # string
        
                self.user_initiative = user_initiative  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetCallRating":
        
        flags = Int.read(b)
        
        user_initiative = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        rating = Int.read(b)
        
        comment = String.read(b)
        
        return SetCallRating(peer=peer, rating=rating, comment=comment, user_initiative=user_initiative)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.rating))
        
        b.write(String(self.comment))
        
        return b.getvalue()