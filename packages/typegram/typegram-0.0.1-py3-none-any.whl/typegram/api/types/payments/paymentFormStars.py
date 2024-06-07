
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



class PaymentFormStars(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.payments.PaymentForm`.

    Details:
        - Layer: ``181``
        - ID: ``7BF6B15C``

form_id (``int`` ``64-bit``):
                    N/A
                
        bot_id (``int`` ``64-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
        description (``str``):
                    N/A
                
        invoice (:obj:`Invoice<typegram.api.ayiin.Invoice>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        photo (:obj:`WebDocument<typegram.api.ayiin.WebDocument>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

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

    __slots__: List[str] = ["form_id", "bot_id", "title", "description", "invoice", "users", "photo"]

    ID = 0x7bf6b15c
    QUALNAME = "functions.typespayments.PaymentForm"

    def __init__(self, *, form_id: int, bot_id: int, title: str, description: str, invoice: "ayiin.Invoice", users: List["ayiin.User"], photo: "ayiin.WebDocument" = None) -> None:
        
                self.form_id = form_id  # long
        
                self.bot_id = bot_id  # long
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.invoice = invoice  # Invoice
        
                self.users = users  # User
        
                self.photo = photo  # WebDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentFormStars":
        
        flags = Int.read(b)
        
        form_id = Long.read(b)
        
        bot_id = Long.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = Object.read(b) if flags & (1 << 5) else None
        
        invoice = Object.read(b)
        
        users = Object.read(b)
        
        return PaymentFormStars(form_id=form_id, bot_id=bot_id, title=title, description=description, invoice=invoice, users=users, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.form_id))
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()