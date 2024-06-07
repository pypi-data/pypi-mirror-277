
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



class CreateChannel(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``91006707``

title (``str``):
                    N/A
                
        about (``str``):
                    N/A
                
        broadcast (``bool``, *optional*):
                    N/A
                
        megagroup (``bool``, *optional*):
                    N/A
                
        for_import (``bool``, *optional*):
                    N/A
                
        forum (``bool``, *optional*):
                    N/A
                
        geo_point (:obj:`InputGeoPoint<typegram.api.ayiin.InputGeoPoint>`, *optional*):
                    N/A
                
        address (``str``, *optional*):
                    N/A
                
        ttl_period (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["title", "about", "broadcast", "megagroup", "for_import", "forum", "geo_point", "address", "ttl_period"]

    ID = 0x91006707
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, title: str, about: str, broadcast: Optional[bool] = None, megagroup: Optional[bool] = None, for_import: Optional[bool] = None, forum: Optional[bool] = None, geo_point: "ayiin.InputGeoPoint" = None, address: Optional[str] = None, ttl_period: Optional[int] = None) -> None:
        
                self.title = title  # string
        
                self.about = about  # string
        
                self.broadcast = broadcast  # true
        
                self.megagroup = megagroup  # true
        
                self.for_import = for_import  # true
        
                self.forum = forum  # true
        
                self.geo_point = geo_point  # InputGeoPoint
        
                self.address = address  # string
        
                self.ttl_period = ttl_period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateChannel":
        
        flags = Int.read(b)
        
        broadcast = True if flags & (1 << 0) else False
        megagroup = True if flags & (1 << 1) else False
        for_import = True if flags & (1 << 3) else False
        forum = True if flags & (1 << 5) else False
        title = String.read(b)
        
        about = String.read(b)
        
        geo_point = Object.read(b) if flags & (1 << 2) else None
        
        address = String.read(b) if flags & (1 << 2) else None
        ttl_period = Int.read(b) if flags & (1 << 4) else None
        return CreateChannel(title=title, about=about, broadcast=broadcast, megagroup=megagroup, for_import=for_import, forum=forum, geo_point=geo_point, address=address, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.about))
        
        if self.geo_point is not None:
            b.write(self.geo_point.write())
        
        if self.address is not None:
            b.write(String(self.address))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()