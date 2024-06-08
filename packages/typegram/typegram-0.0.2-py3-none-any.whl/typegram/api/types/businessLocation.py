
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



class BusinessLocation(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BusinessLocation`.

    Details:
        - Layer: ``181``
        - ID: ``AC5C1AF7``

address (``str``):
                    N/A
                
        geo_point (:obj:`GeoPoint<typegram.api.ayiin.GeoPoint>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["address", "geo_point"]

    ID = 0xac5c1af7
    QUALNAME = "types.businessLocation"

    def __init__(self, *, address: str, geo_point: "api.ayiin.GeoPoint" = None) -> None:
        
                self.address = address  # string
        
                self.geo_point = geo_point  # GeoPoint

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessLocation":
        
        flags = Int.read(b)
        
        geo_point = Object.read(b) if flags & (1 << 0) else None
        
        address = String.read(b)
        
        return BusinessLocation(address=address, geo_point=geo_point)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.geo_point is not None:
            b.write(self.geo_point.write())
        
        b.write(String(self.address))
        
        return b.getvalue()