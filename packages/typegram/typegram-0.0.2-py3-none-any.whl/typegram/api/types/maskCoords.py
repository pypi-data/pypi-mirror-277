
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



class MaskCoords(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MaskCoords`.

    Details:
        - Layer: ``181``
        - ID: ``AED6DBB2``

n (``int`` ``32-bit``):
                    N/A
                
        x (``float`` ``64-bit``):
                    N/A
                
        y (``float`` ``64-bit``):
                    N/A
                
        zoom (``float`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["n", "x", "y", "zoom"]

    ID = 0xaed6dbb2
    QUALNAME = "types.maskCoords"

    def __init__(self, *, n: int, x: float, y: float, zoom: float) -> None:
        
                self.n = n  # int
        
                self.x = x  # double
        
                self.y = y  # double
        
                self.zoom = zoom  # double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MaskCoords":
        # No flags
        
        n = Int.read(b)
        
        x = Double.read(b)
        
        y = Double.read(b)
        
        zoom = Double.read(b)
        
        return MaskCoords(n=n, x=x, y=y, zoom=zoom)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.n))
        
        b.write(Double(self.x))
        
        b.write(Double(self.y))
        
        b.write(Double(self.zoom))
        
        return b.getvalue()