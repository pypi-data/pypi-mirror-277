
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



class GiveawayInfoResults(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.payments.GiveawayInfo`.

    Details:
        - Layer: ``181``
        - ID: ``CD5570``

start_date (``int`` ``32-bit``):
                    N/A
                
        finish_date (``int`` ``32-bit``):
                    N/A
                
        winners_count (``int`` ``32-bit``):
                    N/A
                
        activated_count (``int`` ``32-bit``):
                    N/A
                
        winner (``bool``, *optional*):
                    N/A
                
        refunded (``bool``, *optional*):
                    N/A
                
        gift_code_slug (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 21 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            payments.PaymentForm
            payments.PaymentReceipt
            payments.ValidatedRequestedInfo
            payments.PaymentResult
            payments.BankCardData
            payments.ExportedInvoice
            payments.CheckedGiftCode
            payments.GiveawayInfo
            payments.StarsStatus
    """

    __slots__: List[str] = ["start_date", "finish_date", "winners_count", "activated_count", "winner", "refunded", "gift_code_slug"]

    ID = 0xcd5570
    QUALNAME = "functions.typespayments.GiveawayInfo"

    def __init__(self, *, start_date: int, finish_date: int, winners_count: int, activated_count: int, winner: Optional[bool] = None, refunded: Optional[bool] = None, gift_code_slug: Optional[str] = None) -> None:
        
                self.start_date = start_date  # int
        
                self.finish_date = finish_date  # int
        
                self.winners_count = winners_count  # int
        
                self.activated_count = activated_count  # int
        
                self.winner = winner  # true
        
                self.refunded = refunded  # true
        
                self.gift_code_slug = gift_code_slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GiveawayInfoResults":
        
        flags = Int.read(b)
        
        winner = True if flags & (1 << 0) else False
        refunded = True if flags & (1 << 1) else False
        start_date = Int.read(b)
        
        gift_code_slug = String.read(b) if flags & (1 << 0) else None
        finish_date = Int.read(b)
        
        winners_count = Int.read(b)
        
        activated_count = Int.read(b)
        
        return GiveawayInfoResults(start_date=start_date, finish_date=finish_date, winners_count=winners_count, activated_count=activated_count, winner=winner, refunded=refunded, gift_code_slug=gift_code_slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.start_date))
        
        if self.gift_code_slug is not None:
            b.write(String(self.gift_code_slug))
        
        b.write(Int(self.finish_date))
        
        b.write(Int(self.winners_count))
        
        b.write(Int(self.activated_count))
        
        return b.getvalue()