
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



class SavedInfo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.payments.SavedInfo`.

    Details:
        - Layer: ``181``
        - ID: ``FB8FE43C``

has_saved_credentials (``bool``, *optional*):
                    N/A
                
        saved_info (:obj:`PaymentRequestedInfo<typegram.api.ayiin.PaymentRequestedInfo>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

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

    __slots__: List[str] = ["has_saved_credentials", "saved_info"]

    ID = 0xfb8fe43c
    QUALNAME = "functions.typespayments.SavedInfo"

    def __init__(self, *, has_saved_credentials: Optional[bool] = None, saved_info: "ayiin.PaymentRequestedInfo" = None) -> None:
        
                self.has_saved_credentials = has_saved_credentials  # true
        
                self.saved_info = saved_info  # PaymentRequestedInfo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedInfo":
        
        flags = Int.read(b)
        
        has_saved_credentials = True if flags & (1 << 1) else False
        saved_info = Object.read(b) if flags & (1 << 0) else None
        
        return SavedInfo(has_saved_credentials=has_saved_credentials, saved_info=saved_info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.saved_info is not None:
            b.write(self.saved_info.write())
        
        return b.getvalue()