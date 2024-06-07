
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



class CanPurchasePremium(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9FC19EB6``

purpose (:obj:`InputStorePaymentPurpose<typegram.api.ayiin.InputStorePaymentPurpose>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["purpose"]

    ID = 0x9fc19eb6
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, purpose: "ayiin.InputStorePaymentPurpose") -> None:
        
                self.purpose = purpose  # InputStorePaymentPurpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CanPurchasePremium":
        # No flags
        
        purpose = Object.read(b)
        
        return CanPurchasePremium(purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.purpose.write())
        
        return b.getvalue()