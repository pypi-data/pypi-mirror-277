
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



class ChannelLocation(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelLocation`.

    Details:
        - Layer: ``181``
        - ID: ``209B82DB``

geo_point (:obj:`GeoPoint<typegram.api.ayiin.GeoPoint>`):
                    N/A
                
        address (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["geo_point", "address"]

    ID = 0x209b82db
    QUALNAME = "types.channelLocation"

    def __init__(self, *, geo_point: "api.ayiin.GeoPoint", address: str) -> None:
        
                self.geo_point = geo_point  # GeoPoint
        
                self.address = address  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelLocation":
        # No flags
        
        geo_point = Object.read(b)
        
        address = String.read(b)
        
        return ChannelLocation(geo_point=geo_point, address=address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.geo_point.write())
        
        b.write(String(self.address))
        
        return b.getvalue()