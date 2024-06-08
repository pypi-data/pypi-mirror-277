
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



class SetAccountTTL(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``2442485E``

ttl (:obj:`AccountDaysTTL<typegram.api.ayiin.AccountDaysTTL>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["ttl"]

    ID = 0x2442485e
    QUALNAME = "functions.account.setAccountTTL"

    def __init__(self, *, ttl: "api.ayiin.AccountDaysTTL") -> None:
        
                self.ttl = ttl  # AccountDaysTTL

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetAccountTTL":
        # No flags
        
        ttl = Object.read(b)
        
        return SetAccountTTL(ttl=ttl)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.ttl.write())
        
        return b.getvalue()