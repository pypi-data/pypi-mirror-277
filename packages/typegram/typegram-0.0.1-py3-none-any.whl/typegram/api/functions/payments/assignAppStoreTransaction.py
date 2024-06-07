
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



class AssignAppStoreTransaction(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``80ED747D``

receipt (``bytes``):
                    N/A
                
        purpose (:obj:`InputStorePaymentPurpose<typegram.api.ayiin.InputStorePaymentPurpose>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["receipt", "purpose"]

    ID = 0x80ed747d
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, receipt: bytes, purpose: "ayiin.InputStorePaymentPurpose") -> None:
        
                self.receipt = receipt  # bytes
        
                self.purpose = purpose  # InputStorePaymentPurpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AssignAppStoreTransaction":
        # No flags
        
        receipt = Bytes.read(b)
        
        purpose = Object.read(b)
        
        return AssignAppStoreTransaction(receipt=receipt, purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.receipt))
        
        b.write(self.purpose.write())
        
        return b.getvalue()