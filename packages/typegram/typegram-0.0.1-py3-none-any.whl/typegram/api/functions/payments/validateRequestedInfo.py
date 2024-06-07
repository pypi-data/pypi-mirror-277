
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



class ValidateRequestedInfo(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B6C8F12B``

invoice (:obj:`InputInvoice<typegram.api.ayiin.InputInvoice>`):
                    N/A
                
        info (:obj:`PaymentRequestedInfo<typegram.api.ayiin.PaymentRequestedInfo>`):
                    N/A
                
        save (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`payments.ValidatedRequestedInfo<typegram.api.ayiin.payments.ValidatedRequestedInfo>`
    """

    __slots__: List[str] = ["invoice", "info", "save"]

    ID = 0xb6c8f12b
    QUALNAME = "functions.functionspayments.ValidatedRequestedInfo"

    def __init__(self, *, invoice: "ayiin.InputInvoice", info: "ayiin.PaymentRequestedInfo", save: Optional[bool] = None) -> None:
        
                self.invoice = invoice  # InputInvoice
        
                self.info = info  # PaymentRequestedInfo
        
                self.save = save  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ValidateRequestedInfo":
        
        flags = Int.read(b)
        
        save = True if flags & (1 << 0) else False
        invoice = Object.read(b)
        
        info = Object.read(b)
        
        return ValidateRequestedInfo(invoice=invoice, info=info, save=save)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.invoice.write())
        
        b.write(self.info.write())
        
        return b.getvalue()