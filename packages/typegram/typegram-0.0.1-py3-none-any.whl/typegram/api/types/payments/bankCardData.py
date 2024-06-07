
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



class BankCardData(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.payments.BankCardData`.

    Details:
        - Layer: ``181``
        - ID: ``3E24E573``

title (``str``):
                    N/A
                
        open_urls (List of :obj:`BankCardOpenUrl<typegram.api.ayiin.BankCardOpenUrl>`):
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

    __slots__: List[str] = ["title", "open_urls"]

    ID = 0x3e24e573
    QUALNAME = "functions.typespayments.BankCardData"

    def __init__(self, *, title: str, open_urls: List["ayiin.BankCardOpenUrl"]) -> None:
        
                self.title = title  # string
        
                self.open_urls = open_urls  # BankCardOpenUrl

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BankCardData":
        # No flags
        
        title = String.read(b)
        
        open_urls = Object.read(b)
        
        return BankCardData(title=title, open_urls=open_urls)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.title))
        
        b.write(Vector(self.open_urls))
        
        return b.getvalue()