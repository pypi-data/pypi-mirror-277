
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



class BoostsStatus(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.premium.BoostsStatus`.

    Details:
        - Layer: ``181``
        - ID: ``4959427A``

level (``int`` ``32-bit``):
                    N/A
                
        current_level_boosts (``int`` ``32-bit``):
                    N/A
                
        boosts (``int`` ``32-bit``):
                    N/A
                
        boost_url (``str``):
                    N/A
                
        my_boost (``bool``, *optional*):
                    N/A
                
        gift_boosts (``int`` ``32-bit``, *optional*):
                    N/A
                
        next_level_boosts (``int`` ``32-bit``, *optional*):
                    N/A
                
        premium_audience (:obj:`StatsPercentValue<typegram.api.ayiin.StatsPercentValue>`, *optional*):
                    N/A
                
        prepaid_giveaways (List of :obj:`PrepaidGiveaway<typegram.api.ayiin.PrepaidGiveaway>`, *optional*):
                    N/A
                
        my_boost_slots (List of ``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            premium.BoostsList
            premium.MyBoosts
            premium.BoostsStatus
    """

    __slots__: List[str] = ["level", "current_level_boosts", "boosts", "boost_url", "my_boost", "gift_boosts", "next_level_boosts", "premium_audience", "prepaid_giveaways", "my_boost_slots"]

    ID = 0x4959427a
    QUALNAME = "functions.typespremium.BoostsStatus"

    def __init__(self, *, level: int, current_level_boosts: int, boosts: int, boost_url: str, my_boost: Optional[bool] = None, gift_boosts: Optional[int] = None, next_level_boosts: Optional[int] = None, premium_audience: "ayiin.StatsPercentValue" = None, prepaid_giveaways: Optional[List["ayiin.PrepaidGiveaway"]] = None, my_boost_slots: Optional[List[int]] = None) -> None:
        
                self.level = level  # int
        
                self.current_level_boosts = current_level_boosts  # int
        
                self.boosts = boosts  # int
        
                self.boost_url = boost_url  # string
        
                self.my_boost = my_boost  # true
        
                self.gift_boosts = gift_boosts  # int
        
                self.next_level_boosts = next_level_boosts  # int
        
                self.premium_audience = premium_audience  # StatsPercentValue
        
                self.prepaid_giveaways = prepaid_giveaways  # PrepaidGiveaway
        
                self.my_boost_slots = my_boost_slots  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BoostsStatus":
        
        flags = Int.read(b)
        
        my_boost = True if flags & (1 << 2) else False
        level = Int.read(b)
        
        current_level_boosts = Int.read(b)
        
        boosts = Int.read(b)
        
        gift_boosts = Int.read(b) if flags & (1 << 4) else None
        next_level_boosts = Int.read(b) if flags & (1 << 0) else None
        premium_audience = Object.read(b) if flags & (1 << 1) else None
        
        boost_url = String.read(b)
        
        prepaid_giveaways = Object.read(b) if flags & (1 << 3) else []
        
        my_boost_slots = Object.read(b, Int) if flags & (1 << 2) else []
        
        return BoostsStatus(level=level, current_level_boosts=current_level_boosts, boosts=boosts, boost_url=boost_url, my_boost=my_boost, gift_boosts=gift_boosts, next_level_boosts=next_level_boosts, premium_audience=premium_audience, prepaid_giveaways=prepaid_giveaways, my_boost_slots=my_boost_slots)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.level))
        
        b.write(Int(self.current_level_boosts))
        
        b.write(Int(self.boosts))
        
        if self.gift_boosts is not None:
            b.write(Int(self.gift_boosts))
        
        if self.next_level_boosts is not None:
            b.write(Int(self.next_level_boosts))
        
        if self.premium_audience is not None:
            b.write(self.premium_audience.write())
        
        b.write(String(self.boost_url))
        
        if self.prepaid_giveaways is not None:
            b.write(Vector(self.prepaid_giveaways))
        
        if self.my_boost_slots is not None:
            b.write(Vector(self.my_boost_slots, Int))
        
        return b.getvalue()