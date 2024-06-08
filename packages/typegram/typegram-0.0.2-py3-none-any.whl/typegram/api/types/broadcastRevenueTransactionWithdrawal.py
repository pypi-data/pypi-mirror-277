
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



class BroadcastRevenueTransactionWithdrawal(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BroadcastRevenueTransaction`.

    Details:
        - Layer: ``181``
        - ID: ``5A590978``

amount (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        provider (``str``):
                    N/A
                
        pending (``bool``, *optional*):
                    N/A
                
        failed (``bool``, *optional*):
                    N/A
                
        transaction_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        transaction_url (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["amount", "date", "provider", "pending", "failed", "transaction_date", "transaction_url"]

    ID = 0x5a590978
    QUALNAME = "types.broadcastRevenueTransactionWithdrawal"

    def __init__(self, *, amount: int, date: int, provider: str, pending: Optional[bool] = None, failed: Optional[bool] = None, transaction_date: Optional[int] = None, transaction_url: Optional[str] = None) -> None:
        
                self.amount = amount  # long
        
                self.date = date  # int
        
                self.provider = provider  # string
        
                self.pending = pending  # true
        
                self.failed = failed  # true
        
                self.transaction_date = transaction_date  # int
        
                self.transaction_url = transaction_url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastRevenueTransactionWithdrawal":
        
        flags = Int.read(b)
        
        pending = True if flags & (1 << 0) else False
        failed = True if flags & (1 << 2) else False
        amount = Long.read(b)
        
        date = Int.read(b)
        
        provider = String.read(b)
        
        transaction_date = Int.read(b) if flags & (1 << 1) else None
        transaction_url = String.read(b) if flags & (1 << 1) else None
        return BroadcastRevenueTransactionWithdrawal(amount=amount, date=date, provider=provider, pending=pending, failed=failed, transaction_date=transaction_date, transaction_url=transaction_url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.amount))
        
        b.write(Int(self.date))
        
        b.write(String(self.provider))
        
        if self.transaction_date is not None:
            b.write(Int(self.transaction_date))
        
        if self.transaction_url is not None:
            b.write(String(self.transaction_url))
        
        return b.getvalue()