
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



class GetSecureValue(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``73665BC2``

types (List of :obj:`SecureValueType<typegram.api.ayiin.SecureValueType>`):
                    N/A
                
    Returns:
        List of :obj:`SecureValue<typegram.api.ayiin.SecureValue>`
    """

    __slots__: List[str] = ["types"]

    ID = 0x73665bc2
    QUALNAME = "functions.functions.Vector<SecureValue>"

    def __init__(self, *, types: List["ayiin.SecureValueType"]) -> None:
        
                self.types = types  # SecureValueType

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSecureValue":
        # No flags
        
        types = Object.read(b)
        
        return GetSecureValue(types=types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.types))
        
        return b.getvalue()