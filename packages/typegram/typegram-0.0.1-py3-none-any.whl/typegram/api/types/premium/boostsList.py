
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



class BoostsList(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.premium.BoostsList`.

    Details:
        - Layer: ``181``
        - ID: ``86F8613C``

count (``int`` ``32-bit``):
                    N/A
                
        boosts (List of :obj:`Boost<typegram.api.ayiin.Boost>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        next_offset (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            premium.BoostsList
            premium.MyBoosts
            premium.BoostsStatus
    """

    __slots__: List[str] = ["count", "boosts", "users", "next_offset"]

    ID = 0x86f8613c
    QUALNAME = "functions.typespremium.BoostsList"

    def __init__(self, *, count: int, boosts: List["ayiin.Boost"], users: List["ayiin.User"], next_offset: Optional[str] = None) -> None:
        
                self.count = count  # int
        
                self.boosts = boosts  # Boost
        
                self.users = users  # User
        
                self.next_offset = next_offset  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BoostsList":
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        boosts = Object.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        users = Object.read(b)
        
        return BoostsList(count=count, boosts=boosts, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.boosts))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        b.write(Vector(self.users))
        
        return b.getvalue()