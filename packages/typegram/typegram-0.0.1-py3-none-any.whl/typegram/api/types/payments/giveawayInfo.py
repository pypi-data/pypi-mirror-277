
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



class GiveawayInfo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.payments.GiveawayInfo`.

    Details:
        - Layer: ``181``
        - ID: ``4367DAA0``

start_date (``int`` ``32-bit``):
                    N/A
                
        participating (``bool``, *optional*):
                    N/A
                
        preparing_results (``bool``, *optional*):
                    N/A
                
        joined_too_early_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        admin_disallowed_chat_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        disallowed_country (``str``, *optional*):
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

    __slots__: List[str] = ["start_date", "participating", "preparing_results", "joined_too_early_date", "admin_disallowed_chat_id", "disallowed_country"]

    ID = 0x4367daa0
    QUALNAME = "functions.typespayments.GiveawayInfo"

    def __init__(self, *, start_date: int, participating: Optional[bool] = None, preparing_results: Optional[bool] = None, joined_too_early_date: Optional[int] = None, admin_disallowed_chat_id: Optional[int] = None, disallowed_country: Optional[str] = None) -> None:
        
                self.start_date = start_date  # int
        
                self.participating = participating  # true
        
                self.preparing_results = preparing_results  # true
        
                self.joined_too_early_date = joined_too_early_date  # int
        
                self.admin_disallowed_chat_id = admin_disallowed_chat_id  # long
        
                self.disallowed_country = disallowed_country  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GiveawayInfo":
        
        flags = Int.read(b)
        
        participating = True if flags & (1 << 0) else False
        preparing_results = True if flags & (1 << 3) else False
        start_date = Int.read(b)
        
        joined_too_early_date = Int.read(b) if flags & (1 << 1) else None
        admin_disallowed_chat_id = Long.read(b) if flags & (1 << 2) else None
        disallowed_country = String.read(b) if flags & (1 << 4) else None
        return GiveawayInfo(start_date=start_date, participating=participating, preparing_results=preparing_results, joined_too_early_date=joined_too_early_date, admin_disallowed_chat_id=admin_disallowed_chat_id, disallowed_country=disallowed_country)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.start_date))
        
        if self.joined_too_early_date is not None:
            b.write(Int(self.joined_too_early_date))
        
        if self.admin_disallowed_chat_id is not None:
            b.write(Long(self.admin_disallowed_chat_id))
        
        if self.disallowed_country is not None:
            b.write(String(self.disallowed_country))
        
        return b.getvalue()