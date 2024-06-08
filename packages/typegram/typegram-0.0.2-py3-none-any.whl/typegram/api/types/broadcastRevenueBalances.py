
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



class BroadcastRevenueBalances(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BroadcastRevenueBalances`.

    Details:
        - Layer: ``181``
        - ID: ``8438F1C6``

current_balance (``int`` ``64-bit``):
                    N/A
                
        available_balance (``int`` ``64-bit``):
                    N/A
                
        overall_revenue (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["current_balance", "available_balance", "overall_revenue"]

    ID = 0x8438f1c6
    QUALNAME = "types.broadcastRevenueBalances"

    def __init__(self, *, current_balance: int, available_balance: int, overall_revenue: int) -> None:
        
                self.current_balance = current_balance  # long
        
                self.available_balance = available_balance  # long
        
                self.overall_revenue = overall_revenue  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastRevenueBalances":
        # No flags
        
        current_balance = Long.read(b)
        
        available_balance = Long.read(b)
        
        overall_revenue = Long.read(b)
        
        return BroadcastRevenueBalances(current_balance=current_balance, available_balance=available_balance, overall_revenue=overall_revenue)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.current_balance))
        
        b.write(Long(self.available_balance))
        
        b.write(Long(self.overall_revenue))
        
        return b.getvalue()