
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



class MediaAreaCoordinates(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MediaAreaCoordinates`.

    Details:
        - Layer: ``181``
        - ID: ``3D1EA4E``

x (``float`` ``64-bit``):
                    N/A
                
        y (``float`` ``64-bit``):
                    N/A
                
        w (``float`` ``64-bit``):
                    N/A
                
        h (``float`` ``64-bit``):
                    N/A
                
        rotation (``float`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["x", "y", "w", "h", "rotation"]

    ID = 0x3d1ea4e
    QUALNAME = "types.mediaAreaCoordinates"

    def __init__(self, *, x: float, y: float, w: float, h: float, rotation: float) -> None:
        
                self.x = x  # double
        
                self.y = y  # double
        
                self.w = w  # double
        
                self.h = h  # double
        
                self.rotation = rotation  # double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaCoordinates":
        # No flags
        
        x = Double.read(b)
        
        y = Double.read(b)
        
        w = Double.read(b)
        
        h = Double.read(b)
        
        rotation = Double.read(b)
        
        return MediaAreaCoordinates(x=x, y=y, w=w, h=h, rotation=rotation)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Double(self.x))
        
        b.write(Double(self.y))
        
        b.write(Double(self.w))
        
        b.write(Double(self.h))
        
        b.write(Double(self.rotation))
        
        return b.getvalue()