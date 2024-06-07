
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



class RefundStarsCharge(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``25AE8F4A``

user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        charge_id (``str``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["user_id", "charge_id"]

    ID = 0x25ae8f4a
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, user_id: "ayiin.InputUser", charge_id: str) -> None:
        
                self.user_id = user_id  # InputUser
        
                self.charge_id = charge_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RefundStarsCharge":
        # No flags
        
        user_id = Object.read(b)
        
        charge_id = String.read(b)
        
        return RefundStarsCharge(user_id=user_id, charge_id=charge_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(String(self.charge_id))
        
        return b.getvalue()