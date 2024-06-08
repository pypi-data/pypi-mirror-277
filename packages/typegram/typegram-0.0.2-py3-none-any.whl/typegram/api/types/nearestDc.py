
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



class NearestDc(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.NearestDc`.

    Details:
        - Layer: ``181``
        - ID: ``8E1A1775``

country (``str``):
                    N/A
                
        this_dc (``int`` ``32-bit``):
                    N/A
                
        nearest_dc (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["country", "this_dc", "nearest_dc"]

    ID = 0x8e1a1775
    QUALNAME = "types.nearestDc"

    def __init__(self, *, country: str, this_dc: int, nearest_dc: int) -> None:
        
                self.country = country  # string
        
                self.this_dc = this_dc  # int
        
                self.nearest_dc = nearest_dc  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "NearestDc":
        # No flags
        
        country = String.read(b)
        
        this_dc = Int.read(b)
        
        nearest_dc = Int.read(b)
        
        return NearestDc(country=country, this_dc=this_dc, nearest_dc=nearest_dc)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.country))
        
        b.write(Int(self.this_dc))
        
        b.write(Int(self.nearest_dc))
        
        return b.getvalue()