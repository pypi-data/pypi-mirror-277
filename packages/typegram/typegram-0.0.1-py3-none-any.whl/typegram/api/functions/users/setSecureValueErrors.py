
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



class SetSecureValueErrors(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``90C894B5``

id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        errors (List of :obj:`SecureValueError<typegram.api.ayiin.SecureValueError>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "errors"]

    ID = 0x90c894b5
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, id: "ayiin.InputUser", errors: List["ayiin.SecureValueError"]) -> None:
        
                self.id = id  # InputUser
        
                self.errors = errors  # SecureValueError

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetSecureValueErrors":
        # No flags
        
        id = Object.read(b)
        
        errors = Object.read(b)
        
        return SetSecureValueErrors(id=id, errors=errors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        b.write(Vector(self.errors))
        
        return b.getvalue()