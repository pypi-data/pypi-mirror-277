
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



class BroadcastRevenueTransactionRefund(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BroadcastRevenueTransaction`.

    Details:
        - Layer: ``181``
        - ID: ``42D30D2E``

amount (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        provider (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["amount", "date", "provider"]

    ID = 0x42d30d2e
    QUALNAME = "types.broadcastRevenueTransactionRefund"

    def __init__(self, *, amount: int, date: int, provider: str) -> None:
        
                self.amount = amount  # long
        
                self.date = date  # int
        
                self.provider = provider  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastRevenueTransactionRefund":
        # No flags
        
        amount = Long.read(b)
        
        date = Int.read(b)
        
        provider = String.read(b)
        
        return BroadcastRevenueTransactionRefund(amount=amount, date=date, provider=provider)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.amount))
        
        b.write(Int(self.date))
        
        b.write(String(self.provider))
        
        return b.getvalue()