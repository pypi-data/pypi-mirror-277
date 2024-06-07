
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



class SentCodeTypeMissedCall(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.SentCodeType`.

    Details:
        - Layer: ``181``
        - ID: ``82006484``

prefix (``str``):
                    N/A
                
        length (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            auth.SentCode
            auth.Authorization
            auth.ExportedAuthorization
            auth.LoginToken
    """

    __slots__: List[str] = ["prefix", "length"]

    ID = 0x82006484
    QUALNAME = "functions.typesauth.SentCodeType"

    def __init__(self, *, prefix: str, length: int) -> None:
        
                self.prefix = prefix  # string
        
                self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeMissedCall":
        # No flags
        
        prefix = String.read(b)
        
        length = Int.read(b)
        
        return SentCodeTypeMissedCall(prefix=prefix, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.prefix))
        
        b.write(Int(self.length))
        
        return b.getvalue()