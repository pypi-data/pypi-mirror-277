
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



class AcceptLoginToken(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E894AD4D``

token (``bytes``):
                    N/A
                
    Returns:
        :obj:`Authorization<typegram.api.ayiin.Authorization>`
    """

    __slots__: List[str] = ["token"]

    ID = 0xe894ad4d
    QUALNAME = "functions.auth.acceptLoginToken"

    def __init__(self, *, token: bytes) -> None:
        
                self.token = token  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptLoginToken":
        # No flags
        
        token = Bytes.read(b)
        
        return AcceptLoginToken(token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.token))
        
        return b.getvalue()