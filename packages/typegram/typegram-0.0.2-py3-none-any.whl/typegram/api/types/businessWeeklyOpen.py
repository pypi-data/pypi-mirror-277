
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



class BusinessWeeklyOpen(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BusinessWeeklyOpen`.

    Details:
        - Layer: ``181``
        - ID: ``120B1AB9``

start_minute (``int`` ``32-bit``):
                    N/A
                
        end_minute (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["start_minute", "end_minute"]

    ID = 0x120b1ab9
    QUALNAME = "types.businessWeeklyOpen"

    def __init__(self, *, start_minute: int, end_minute: int) -> None:
        
                self.start_minute = start_minute  # int
        
                self.end_minute = end_minute  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessWeeklyOpen":
        # No flags
        
        start_minute = Int.read(b)
        
        end_minute = Int.read(b)
        
        return BusinessWeeklyOpen(start_minute=start_minute, end_minute=end_minute)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.start_minute))
        
        b.write(Int(self.end_minute))
        
        return b.getvalue()