
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



class SendPaymentForm(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``2D03522F``

form_id (``int`` ``64-bit``):
                    N/A
                
        invoice (:obj:`InputInvoice<typegram.api.ayiin.InputInvoice>`):
                    N/A
                
        credentials (:obj:`InputPaymentCredentials<typegram.api.ayiin.InputPaymentCredentials>`):
                    N/A
                
        requested_info_id (``str``, *optional*):
                    N/A
                
        shipping_option_id (``str``, *optional*):
                    N/A
                
        tip_amount (``int`` ``64-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`payments.PaymentResult<typegram.api.ayiin.payments.PaymentResult>`
    """

    __slots__: List[str] = ["form_id", "invoice", "credentials", "requested_info_id", "shipping_option_id", "tip_amount"]

    ID = 0x2d03522f
    QUALNAME = "functions.functionspayments.PaymentResult"

    def __init__(self, *, form_id: int, invoice: "ayiin.InputInvoice", credentials: "ayiin.InputPaymentCredentials", requested_info_id: Optional[str] = None, shipping_option_id: Optional[str] = None, tip_amount: Optional[int] = None) -> None:
        
                self.form_id = form_id  # long
        
                self.invoice = invoice  # InputInvoice
        
                self.credentials = credentials  # InputPaymentCredentials
        
                self.requested_info_id = requested_info_id  # string
        
                self.shipping_option_id = shipping_option_id  # string
        
                self.tip_amount = tip_amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendPaymentForm":
        
        flags = Int.read(b)
        
        form_id = Long.read(b)
        
        invoice = Object.read(b)
        
        requested_info_id = String.read(b) if flags & (1 << 0) else None
        shipping_option_id = String.read(b) if flags & (1 << 1) else None
        credentials = Object.read(b)
        
        tip_amount = Long.read(b) if flags & (1 << 2) else None
        return SendPaymentForm(form_id=form_id, invoice=invoice, credentials=credentials, requested_info_id=requested_info_id, shipping_option_id=shipping_option_id, tip_amount=tip_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.form_id))
        
        b.write(self.invoice.write())
        
        if self.requested_info_id is not None:
            b.write(String(self.requested_info_id))
        
        if self.shipping_option_id is not None:
            b.write(String(self.shipping_option_id))
        
        b.write(self.credentials.write())
        
        if self.tip_amount is not None:
            b.write(Long(self.tip_amount))
        
        return b.getvalue()