
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



class SetDefaultHistoryTTL(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9EB51445``

period (``int`` ``32-bit``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["period"]

    ID = 0x9eb51445
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, period: int) -> None:
        
                self.period = period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetDefaultHistoryTTL":
        # No flags
        
        period = Int.read(b)
        
        return SetDefaultHistoryTTL(period=period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.period))
        
        return b.getvalue()