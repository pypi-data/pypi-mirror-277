
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



class BusinessAwayMessageScheduleCustom(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BusinessAwayMessageSchedule`.

    Details:
        - Layer: ``181``
        - ID: ``CC4D9ECC``

start_date (``int`` ``32-bit``):
                    N/A
                
        end_date (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["start_date", "end_date"]

    ID = 0xcc4d9ecc
    QUALNAME = "types.businessAwayMessageScheduleCustom"

    def __init__(self, *, start_date: int, end_date: int) -> None:
        
                self.start_date = start_date  # int
        
                self.end_date = end_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessAwayMessageScheduleCustom":
        # No flags
        
        start_date = Int.read(b)
        
        end_date = Int.read(b)
        
        return BusinessAwayMessageScheduleCustom(start_date=start_date, end_date=end_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.start_date))
        
        b.write(Int(self.end_date))
        
        return b.getvalue()