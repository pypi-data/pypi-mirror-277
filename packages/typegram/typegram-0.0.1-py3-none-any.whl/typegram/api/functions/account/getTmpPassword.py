
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



class GetTmpPassword(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``449E0B51``

password (:obj:`InputCheckPasswordSRP<typegram.api.ayiin.InputCheckPasswordSRP>`):
                    N/A
                
        period (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`account.TmpPassword<typegram.api.ayiin.account.TmpPassword>`
    """

    __slots__: List[str] = ["password", "period"]

    ID = 0x449e0b51
    QUALNAME = "functions.functionsaccount.TmpPassword"

    def __init__(self, *, password: "ayiin.InputCheckPasswordSRP", period: int) -> None:
        
                self.password = password  # InputCheckPasswordSRP
        
                self.period = period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTmpPassword":
        # No flags
        
        password = Object.read(b)
        
        period = Int.read(b)
        
        return GetTmpPassword(password=password, period=period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.password.write())
        
        b.write(Int(self.period))
        
        return b.getvalue()