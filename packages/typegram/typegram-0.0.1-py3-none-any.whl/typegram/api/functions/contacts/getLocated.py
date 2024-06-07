
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



class GetLocated(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D348BC44``

geo_point (:obj:`InputGeoPoint<typegram.api.ayiin.InputGeoPoint>`):
                    N/A
                
        background (``bool``, *optional*):
                    N/A
                
        is_self_expires (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["geo_point", "background", "is_self_expires"]

    ID = 0xd348bc44
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, geo_point: "ayiin.InputGeoPoint", background: Optional[bool] = None, is_self_expires: Optional[int] = None) -> None:
        
                self.geo_point = geo_point  # InputGeoPoint
        
                self.background = background  # true
        
                self.is_self_expires = is_self_expires  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetLocated":
        
        flags = Int.read(b)
        
        background = True if flags & (1 << 1) else False
        geo_point = Object.read(b)
        
        is_self_expires = Int.read(b) if flags & (1 << 0) else None
        return GetLocated(geo_point=geo_point, background=background, is_self_expires=is_self_expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.geo_point.write())
        
        if self.is_self_expires is not None:
            b.write(Int(self.is_self_expires))
        
        return b.getvalue()