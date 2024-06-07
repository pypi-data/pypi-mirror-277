
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



class InvokeWithApnsSecret(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``0DAE54F8``

nonce (``str``):
                    N/A
                
        secret (``str``):
                    N/A
                
        query (``!x``):
                    N/A
                
    Returns:
        Any object from :obj:`~typegram.api.types`
    """

    __slots__: List[str] = ["nonce", "secret", "query"]

    ID = 0x0dae54f8
    QUALNAME = "functions.functions.X"

    def __init__(self, *, nonce: str, secret: str, query: bytes) -> None:
        
                self.nonce = nonce  # string
        
                self.secret = secret  # string
        
                self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithApnsSecret":
        # No flags
        
        nonce = String.read(b)
        
        secret = String.read(b)
        
        query = !X.read(b)
        
        return InvokeWithApnsSecret(nonce=nonce, secret=secret, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.nonce))
        
        b.write(String(self.secret))
        
        b.write(!X(self.query))
        
        return b.getvalue()