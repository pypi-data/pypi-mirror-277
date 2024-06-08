
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



class StatsPercentValue(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StatsPercentValue`.

    Details:
        - Layer: ``181``
        - ID: ``CBCE2FE0``

part (``float`` ``64-bit``):
                    N/A
                
        total (``float`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["part", "total"]

    ID = 0xcbce2fe0
    QUALNAME = "types.statsPercentValue"

    def __init__(self, *, part: float, total: float) -> None:
        
                self.part = part  # double
        
                self.total = total  # double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsPercentValue":
        # No flags
        
        part = Double.read(b)
        
        total = Double.read(b)
        
        return StatsPercentValue(part=part, total=total)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Double(self.part))
        
        b.write(Double(self.total))
        
        return b.getvalue()