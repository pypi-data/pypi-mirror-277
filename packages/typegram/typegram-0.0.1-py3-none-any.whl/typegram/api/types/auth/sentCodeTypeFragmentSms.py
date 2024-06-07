
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



class SentCodeTypeFragmentSms(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.SentCodeType`.

    Details:
        - Layer: ``181``
        - ID: ``D9565C39``

url (``str``):
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

    __slots__: List[str] = ["url", "length"]

    ID = 0xd9565c39
    QUALNAME = "functions.typesauth.SentCodeType"

    def __init__(self, *, url: str, length: int) -> None:
        
                self.url = url  # string
        
                self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeFragmentSms":
        # No flags
        
        url = String.read(b)
        
        length = Int.read(b)
        
        return SentCodeTypeFragmentSms(url=url, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Int(self.length))
        
        return b.getvalue()