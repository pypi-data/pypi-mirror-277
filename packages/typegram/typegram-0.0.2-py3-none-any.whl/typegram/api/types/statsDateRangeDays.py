
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



class StatsDateRangeDays(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StatsDateRangeDays`.

    Details:
        - Layer: ``181``
        - ID: ``B637EDAF``

min_date (``int`` ``32-bit``):
                    N/A
                
        max_date (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["min_date", "max_date"]

    ID = 0xb637edaf
    QUALNAME = "types.statsDateRangeDays"

    def __init__(self, *, min_date: int, max_date: int) -> None:
        
                self.min_date = min_date  # int
        
                self.max_date = max_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsDateRangeDays":
        # No flags
        
        min_date = Int.read(b)
        
        max_date = Int.read(b)
        
        return StatsDateRangeDays(min_date=min_date, max_date=max_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.min_date))
        
        b.write(Int(self.max_date))
        
        return b.getvalue()