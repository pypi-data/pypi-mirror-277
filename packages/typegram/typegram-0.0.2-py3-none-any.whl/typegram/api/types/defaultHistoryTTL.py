
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



class DefaultHistoryTTL(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.DefaultHistoryTTL`.

    Details:
        - Layer: ``181``
        - ID: ``43B46B20``

period (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["period"]

    ID = 0x43b46b20
    QUALNAME = "types.defaultHistoryTTL"

    def __init__(self, *, period: int) -> None:
        
                self.period = period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DefaultHistoryTTL":
        # No flags
        
        period = Int.read(b)
        
        return DefaultHistoryTTL(period=period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.period))
        
        return b.getvalue()