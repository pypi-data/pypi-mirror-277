
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



class MediaAreaVenue(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MediaArea`.

    Details:
        - Layer: ``181``
        - ID: ``BE82DB9C``

coordinates (:obj:`MediaAreaCoordinates<typegram.api.ayiin.MediaAreaCoordinates>`):
                    N/A
                
        geo (:obj:`GeoPoint<typegram.api.ayiin.GeoPoint>`):
                    N/A
                
        title (``str``):
                    N/A
                
        address (``str``):
                    N/A
                
        provider (``str``):
                    N/A
                
        venue_id (``str``):
                    N/A
                
        venue_type (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["coordinates", "geo", "title", "address", "provider", "venue_id", "venue_type"]

    ID = 0xbe82db9c
    QUALNAME = "types.mediaAreaVenue"

    def __init__(self, *, coordinates: "api.ayiin.MediaAreaCoordinates", geo: "api.ayiin.GeoPoint", title: str, address: str, provider: str, venue_id: str, venue_type: str) -> None:
        
                self.coordinates = coordinates  # MediaAreaCoordinates
        
                self.geo = geo  # GeoPoint
        
                self.title = title  # string
        
                self.address = address  # string
        
                self.provider = provider  # string
        
                self.venue_id = venue_id  # string
        
                self.venue_type = venue_type  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaVenue":
        # No flags
        
        coordinates = Object.read(b)
        
        geo = Object.read(b)
        
        title = String.read(b)
        
        address = String.read(b)
        
        provider = String.read(b)
        
        venue_id = String.read(b)
        
        venue_type = String.read(b)
        
        return MediaAreaVenue(coordinates=coordinates, geo=geo, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.coordinates.write())
        
        b.write(self.geo.write())
        
        b.write(String(self.title))
        
        b.write(String(self.address))
        
        b.write(String(self.provider))
        
        b.write(String(self.venue_id))
        
        b.write(String(self.venue_type))
        
        return b.getvalue()