
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



class SaveSecureValue(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``899FE31D``

value (:obj:`InputSecureValue<typegram.api.ayiin.InputSecureValue>`):
                    N/A
                
        secure_secret_id (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`SecureValue<typegram.api.ayiin.SecureValue>`
    """

    __slots__: List[str] = ["value", "secure_secret_id"]

    ID = 0x899fe31d
    QUALNAME = "functions.functions.SecureValue"

    def __init__(self, *, value: "ayiin.InputSecureValue", secure_secret_id: int) -> None:
        
                self.value = value  # InputSecureValue
        
                self.secure_secret_id = secure_secret_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveSecureValue":
        # No flags
        
        value = Object.read(b)
        
        secure_secret_id = Long.read(b)
        
        return SaveSecureValue(value=value, secure_secret_id=secure_secret_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.value.write())
        
        b.write(Long(self.secure_secret_id))
        
        return b.getvalue()