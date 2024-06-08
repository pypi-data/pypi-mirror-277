
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class InputInvoicePremiumGiftCode(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputInvoice`.

    Details:
        - Layer: ``181``
        - ID: ``98986C0D``

purpose (:obj:`InputStorePaymentPurpose<typegram.api.ayiin.InputStorePaymentPurpose>`):
                    N/A
                
        option (:obj:`PremiumGiftCodeOption<typegram.api.ayiin.PremiumGiftCodeOption>`):
                    N/A
                
    """

    __slots__: List[str] = ["purpose", "option"]

    ID = 0x98986c0d
    QUALNAME = "types.inputInvoicePremiumGiftCode"

    def __init__(self, *, purpose: "api.ayiin.InputStorePaymentPurpose", option: "api.ayiin.PremiumGiftCodeOption") -> None:
        
                self.purpose = purpose  # InputStorePaymentPurpose
        
                self.option = option  # PremiumGiftCodeOption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoicePremiumGiftCode":
        # No flags
        
        purpose = Object.read(b)
        
        option = Object.read(b)
        
        return InputInvoicePremiumGiftCode(purpose=purpose, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.purpose.write())
        
        b.write(self.option.write())
        
        return b.getvalue()