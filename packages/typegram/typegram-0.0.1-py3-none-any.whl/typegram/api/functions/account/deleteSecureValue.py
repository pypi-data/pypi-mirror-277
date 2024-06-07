
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



class DeleteSecureValue(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B880BC4B``

types (List of :obj:`SecureValueType<typegram.api.ayiin.SecureValueType>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["types"]

    ID = 0xb880bc4b
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, types: List["ayiin.SecureValueType"]) -> None:
        
                self.types = types  # SecureValueType

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteSecureValue":
        # No flags
        
        types = Object.read(b)
        
        return DeleteSecureValue(types=types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.types))
        
        return b.getvalue()