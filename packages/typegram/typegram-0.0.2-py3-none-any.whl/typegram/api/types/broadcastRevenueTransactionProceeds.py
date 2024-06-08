
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



class BroadcastRevenueTransactionProceeds(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BroadcastRevenueTransaction`.

    Details:
        - Layer: ``181``
        - ID: ``557E2CC4``

amount (``int`` ``64-bit``):
                    N/A
                
        from_date (``int`` ``32-bit``):
                    N/A
                
        to_date (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["amount", "from_date", "to_date"]

    ID = 0x557e2cc4
    QUALNAME = "types.broadcastRevenueTransactionProceeds"

    def __init__(self, *, amount: int, from_date: int, to_date: int) -> None:
        
                self.amount = amount  # long
        
                self.from_date = from_date  # int
        
                self.to_date = to_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastRevenueTransactionProceeds":
        # No flags
        
        amount = Long.read(b)
        
        from_date = Int.read(b)
        
        to_date = Int.read(b)
        
        return BroadcastRevenueTransactionProceeds(amount=amount, from_date=from_date, to_date=to_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.amount))
        
        b.write(Int(self.from_date))
        
        b.write(Int(self.to_date))
        
        return b.getvalue()