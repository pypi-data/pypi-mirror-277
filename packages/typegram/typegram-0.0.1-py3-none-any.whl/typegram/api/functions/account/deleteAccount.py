
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



class DeleteAccount(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A2C0CF74``

reason (``str``):
                    N/A
                
        password (:obj:`InputCheckPasswordSRP<typegram.api.ayiin.InputCheckPasswordSRP>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["reason", "password"]

    ID = 0xa2c0cf74
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, reason: str, password: "ayiin.InputCheckPasswordSRP" = None) -> None:
        
                self.reason = reason  # string
        
                self.password = password  # InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteAccount":
        
        flags = Int.read(b)
        
        reason = String.read(b)
        
        password = Object.read(b) if flags & (1 << 0) else None
        
        return DeleteAccount(reason=reason, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.reason))
        
        if self.password is not None:
            b.write(self.password.write())
        
        return b.getvalue()