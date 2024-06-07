
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



class BroadcastRevenueTransactions(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stats.BroadcastRevenueTransactions`.

    Details:
        - Layer: ``181``
        - ID: ``87158466``

count (``int`` ``32-bit``):
                    N/A
                
        transactions (List of :obj:`BroadcastRevenueTransaction<typegram.api.ayiin.BroadcastRevenueTransaction>`):
                    N/A
                
    Functions:
        This object can be returned by 34 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            stats.BroadcastStats
            stats.MegagroupStats
            stats.PublicForwards
            stats.MessageStats
            stats.StoryStats
            stats.BroadcastRevenueStats
            stats.BroadcastRevenueWithdrawalUrl
            stats.BroadcastRevenueTransactions
    """

    __slots__: List[str] = ["count", "transactions"]

    ID = 0x87158466
    QUALNAME = "functions.typesstats.BroadcastRevenueTransactions"

    def __init__(self, *, count: int, transactions: List["ayiin.BroadcastRevenueTransaction"]) -> None:
        
                self.count = count  # int
        
                self.transactions = transactions  # BroadcastRevenueTransaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastRevenueTransactions":
        # No flags
        
        count = Int.read(b)
        
        transactions = Object.read(b)
        
        return BroadcastRevenueTransactions(count=count, transactions=transactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.transactions))
        
        return b.getvalue()