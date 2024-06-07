
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



class GetPaymentForm(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``37148DBB``

invoice (:obj:`InputInvoice<typegram.api.ayiin.InputInvoice>`):
                    N/A
                
        theme_params (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`, *optional*):
                    N/A
                
    Returns:
        :obj:`payments.PaymentForm<typegram.api.ayiin.payments.PaymentForm>`
    """

    __slots__: List[str] = ["invoice", "theme_params"]

    ID = 0x37148dbb
    QUALNAME = "functions.functionspayments.PaymentForm"

    def __init__(self, *, invoice: "ayiin.InputInvoice", theme_params: "ayiin.DataJSON" = None) -> None:
        
                self.invoice = invoice  # InputInvoice
        
                self.theme_params = theme_params  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPaymentForm":
        
        flags = Int.read(b)
        
        invoice = Object.read(b)
        
        theme_params = Object.read(b) if flags & (1 << 0) else None
        
        return GetPaymentForm(invoice=invoice, theme_params=theme_params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.invoice.write())
        
        if self.theme_params is not None:
            b.write(self.theme_params.write())
        
        return b.getvalue()