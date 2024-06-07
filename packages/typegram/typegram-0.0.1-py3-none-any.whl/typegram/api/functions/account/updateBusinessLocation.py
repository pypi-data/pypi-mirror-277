
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



class UpdateBusinessLocation(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9E6B131A``

geo_point (:obj:`InputGeoPoint<typegram.api.ayiin.InputGeoPoint>`, *optional*):
                    N/A
                
        address (``str``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["geo_point", "address"]

    ID = 0x9e6b131a
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, geo_point: "ayiin.InputGeoPoint" = None, address: Optional[str] = None) -> None:
        
                self.geo_point = geo_point  # InputGeoPoint
        
                self.address = address  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessLocation":
        
        flags = Int.read(b)
        
        geo_point = Object.read(b) if flags & (1 << 1) else None
        
        address = String.read(b) if flags & (1 << 0) else None
        return UpdateBusinessLocation(geo_point=geo_point, address=address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.geo_point is not None:
            b.write(self.geo_point.write())
        
        if self.address is not None:
            b.write(String(self.address))
        
        return b.getvalue()