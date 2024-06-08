
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



class PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PasswordKdfAlgo`.

    Details:
        - Layer: ``181``
        - ID: ``3A912D4A``

salt1 (``bytes``):
                    N/A
                
        salt2 (``bytes``):
                    N/A
                
        g (``int`` ``32-bit``):
                    N/A
                
        p (``bytes``):
                    N/A
                
    """

    __slots__: List[str] = ["salt1", "salt2", "g", "p"]

    ID = 0x3a912d4a
    QUALNAME = "types.passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow"

    def __init__(self, *, salt1: bytes, salt2: bytes, g: int, p: bytes) -> None:
        
                self.salt1 = salt1  # bytes
        
                self.salt2 = salt2  # bytes
        
                self.g = g  # int
        
                self.p = p  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow":
        # No flags
        
        salt1 = Bytes.read(b)
        
        salt2 = Bytes.read(b)
        
        g = Int.read(b)
        
        p = Bytes.read(b)
        
        return PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow(salt1=salt1, salt2=salt2, g=g, p=p)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.salt1))
        
        b.write(Bytes(self.salt2))
        
        b.write(Int(self.g))
        
        b.write(Bytes(self.p))
        
        return b.getvalue()