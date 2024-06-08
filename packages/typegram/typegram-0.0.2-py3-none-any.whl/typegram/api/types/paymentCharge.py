
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



class PaymentCharge(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PaymentCharge`.

    Details:
        - Layer: ``181``
        - ID: ``EA02C27E``

id (``str``):
                    N/A
                
        provider_charge_id (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["id", "provider_charge_id"]

    ID = 0xea02c27e
    QUALNAME = "types.paymentCharge"

    def __init__(self, *, id: str, provider_charge_id: str) -> None:
        
                self.id = id  # string
        
                self.provider_charge_id = provider_charge_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentCharge":
        # No flags
        
        id = String.read(b)
        
        provider_charge_id = String.read(b)
        
        return PaymentCharge(id=id, provider_charge_id=provider_charge_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.id))
        
        b.write(String(self.provider_charge_id))
        
        return b.getvalue()