
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



class ImportAuthorization(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A57A7DAD``

id (``int`` ``64-bit``):
                    N/A
                
        bytes (``bytes``):
                    N/A
                
    Returns:
        :obj:`auth.Authorization<typegram.api.ayiin.auth.Authorization>`
    """

    __slots__: List[str] = ["id", "bytes"]

    ID = 0xa57a7dad
    QUALNAME = "functions.functionsauth.Authorization"

    def __init__(self, *, id: int, bytes: bytes) -> None:
        
                self.id = id  # long
        
                self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportAuthorization":
        # No flags
        
        id = Long.read(b)
        
        bytes = Bytes.read(b)
        
        return ImportAuthorization(id=id, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()