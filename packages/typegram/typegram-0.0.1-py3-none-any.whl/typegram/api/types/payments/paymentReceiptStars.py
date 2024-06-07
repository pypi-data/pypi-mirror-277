
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



class PaymentReceiptStars(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.payments.PaymentReceipt`.

    Details:
        - Layer: ``181``
        - ID: ``DABBF83A``

date (``int`` ``32-bit``):
                    N/A
                
        bot_id (``int`` ``64-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
        description (``str``):
                    N/A
                
        invoice (:obj:`Invoice<typegram.api.ayiin.Invoice>`):
                    N/A
                
        currency (``str``):
                    N/A
                
        total_amount (``int`` ``64-bit``):
                    N/A
                
        transaction_id (``str``):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        photo (:obj:`WebDocument<typegram.api.ayiin.WebDocument>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 23 functions.

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

    __slots__: List[str] = ["date", "bot_id", "title", "description", "invoice", "currency", "total_amount", "transaction_id", "users", "photo"]

    ID = 0xdabbf83a
    QUALNAME = "functions.typespayments.PaymentReceipt"

    def __init__(self, *, date: int, bot_id: int, title: str, description: str, invoice: "ayiin.Invoice", currency: str, total_amount: int, transaction_id: str, users: List["ayiin.User"], photo: "ayiin.WebDocument" = None) -> None:
        
                self.date = date  # int
        
                self.bot_id = bot_id  # long
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.invoice = invoice  # Invoice
        
                self.currency = currency  # string
        
                self.total_amount = total_amount  # long
        
                self.transaction_id = transaction_id  # string
        
                self.users = users  # User
        
                self.photo = photo  # WebDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentReceiptStars":
        
        flags = Int.read(b)
        
        date = Int.read(b)
        
        bot_id = Long.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = Object.read(b) if flags & (1 << 2) else None
        
        invoice = Object.read(b)
        
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        transaction_id = String.read(b)
        
        users = Object.read(b)
        
        return PaymentReceiptStars(date=date, bot_id=bot_id, title=title, description=description, invoice=invoice, currency=currency, total_amount=total_amount, transaction_id=transaction_id, users=users, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.date))
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        b.write(String(self.transaction_id))
        
        b.write(Vector(self.users))
        
        return b.getvalue()