
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



class ExportInvoice(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F91B065``

invoice_media (:obj:`InputMedia<typegram.api.ayiin.InputMedia>`):
                    N/A
                
    Returns:
        :obj:`payments.ExportedInvoice<typegram.api.ayiin.payments.ExportedInvoice>`
    """

    __slots__: List[str] = ["invoice_media"]

    ID = 0xf91b065
    QUALNAME = "functions.functionspayments.ExportedInvoice"

    def __init__(self, *, invoice_media: "ayiin.InputMedia") -> None:
        
                self.invoice_media = invoice_media  # InputMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportInvoice":
        # No flags
        
        invoice_media = Object.read(b)
        
        return ExportInvoice(invoice_media=invoice_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.invoice_media.write())
        
        return b.getvalue()