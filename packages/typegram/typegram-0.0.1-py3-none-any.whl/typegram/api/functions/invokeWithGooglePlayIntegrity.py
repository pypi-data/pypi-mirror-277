
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



class InvokeWithGooglePlayIntegrity(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``1DF92984``

nonce (``str``):
                    N/A
                
        token (``str``):
                    N/A
                
        query (``!x``):
                    N/A
                
    Returns:
        Any object from :obj:`~typegram.api.types`
    """

    __slots__: List[str] = ["nonce", "token", "query"]

    ID = 0x1df92984
    QUALNAME = "functions.functions.X"

    def __init__(self, *, nonce: str, token: str, query: bytes) -> None:
        
                self.nonce = nonce  # string
        
                self.token = token  # string
        
                self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithGooglePlayIntegrity":
        # No flags
        
        nonce = String.read(b)
        
        token = String.read(b)
        
        query = !X.read(b)
        
        return InvokeWithGooglePlayIntegrity(nonce=nonce, token=token, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.nonce))
        
        b.write(String(self.token))
        
        b.write(!X(self.query))
        
        return b.getvalue()