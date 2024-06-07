
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



class ImportLoginToken(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``95AC5CE4``

token (``bytes``):
                    N/A
                
    Returns:
        :obj:`auth.LoginToken<typegram.api.ayiin.auth.LoginToken>`
    """

    __slots__: List[str] = ["token"]

    ID = 0x95ac5ce4
    QUALNAME = "functions.functionsauth.LoginToken"

    def __init__(self, *, token: bytes) -> None:
        
                self.token = token  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportLoginToken":
        # No flags
        
        token = Bytes.read(b)
        
        return ImportLoginToken(token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.token))
        
        return b.getvalue()