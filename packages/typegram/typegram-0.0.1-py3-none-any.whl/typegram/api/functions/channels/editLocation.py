
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



class EditLocation(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``58E63F6D``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        geo_point (:obj:`InputGeoPoint<typegram.api.ayiin.InputGeoPoint>`):
                    N/A
                
        address (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "geo_point", "address"]

    ID = 0x58e63f6d
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, channel: "ayiin.InputChannel", geo_point: "ayiin.InputGeoPoint", address: str) -> None:
        
                self.channel = channel  # InputChannel
        
                self.geo_point = geo_point  # InputGeoPoint
        
                self.address = address  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditLocation":
        # No flags
        
        channel = Object.read(b)
        
        geo_point = Object.read(b)
        
        address = String.read(b)
        
        return EditLocation(channel=channel, geo_point=geo_point, address=address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.geo_point.write())
        
        b.write(String(self.address))
        
        return b.getvalue()