
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



class SetAuthorizationTTL(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``BF899AA0``

authorization_ttl_days (``int`` ``32-bit``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["authorization_ttl_days"]

    ID = 0xbf899aa0
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, authorization_ttl_days: int) -> None:
        
                self.authorization_ttl_days = authorization_ttl_days  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetAuthorizationTTL":
        # No flags
        
        authorization_ttl_days = Int.read(b)
        
        return SetAuthorizationTTL(authorization_ttl_days=authorization_ttl_days)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.authorization_ttl_days))
        
        return b.getvalue()