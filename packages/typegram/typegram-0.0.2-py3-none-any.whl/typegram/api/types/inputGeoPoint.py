
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



class InputGeoPoint(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputGeoPoint`.

    Details:
        - Layer: ``181``
        - ID: ``48222FAF``

lat (``float`` ``64-bit``):
                    N/A
                
        long (``float`` ``64-bit``):
                    N/A
                
        accuracy_radius (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["lat", "long", "accuracy_radius"]

    ID = 0x48222faf
    QUALNAME = "types.inputGeoPoint"

    def __init__(self, *, lat: float, long: float, accuracy_radius: Optional[int] = None) -> None:
        
                self.lat = lat  # double
        
                self.long = long  # double
        
                self.accuracy_radius = accuracy_radius  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGeoPoint":
        
        flags = Int.read(b)
        
        lat = Double.read(b)
        
        long = Double.read(b)
        
        accuracy_radius = Int.read(b) if flags & (1 << 0) else None
        return InputGeoPoint(lat=lat, long=long, accuracy_radius=accuracy_radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Double(self.lat))
        
        b.write(Double(self.long))
        
        if self.accuracy_radius is not None:
            b.write(Int(self.accuracy_radius))
        
        return b.getvalue()