
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



class SecureValueHash(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SecureValueHash`.

    Details:
        - Layer: ``181``
        - ID: ``ED1ECDB0``

type (:obj:`SecureValueType<typegram.api.ayiin.SecureValueType>`):
                    N/A
                
        hash (``bytes``):
                    N/A
                
    """

    __slots__: List[str] = ["type", "hash"]

    ID = 0xed1ecdb0
    QUALNAME = "types.secureValueHash"

    def __init__(self, *, type: "api.ayiin.SecureValueType", hash: bytes) -> None:
        
                self.type = type  # SecureValueType
        
                self.hash = hash  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueHash":
        # No flags
        
        type = Object.read(b)
        
        hash = Bytes.read(b)
        
        return SecureValueHash(type=type, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.type.write())
        
        b.write(Bytes(self.hash))
        
        return b.getvalue()