
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



class SendStarsForm(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``2BB731D``

form_id (``int`` ``64-bit``):
                    N/A
                
        invoice (:obj:`InputInvoice<typegram.api.ayiin.InputInvoice>`):
                    N/A
                
    Returns:
        :obj:`payments.PaymentResult<typegram.api.ayiin.payments.PaymentResult>`
    """

    __slots__: List[str] = ["form_id", "invoice"]

    ID = 0x2bb731d
    QUALNAME = "functions.functionspayments.PaymentResult"

    def __init__(self, *, form_id: int, invoice: "ayiin.InputInvoice") -> None:
        
                self.form_id = form_id  # long
        
                self.invoice = invoice  # InputInvoice

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendStarsForm":
        
        flags = Int.read(b)
        
        form_id = Long.read(b)
        
        invoice = Object.read(b)
        
        return SendStarsForm(form_id=form_id, invoice=invoice)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.form_id))
        
        b.write(self.invoice.write())
        
        return b.getvalue()