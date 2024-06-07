
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



class GetDocumentByHash(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B1F2061F``

sha256 (``bytes``):
                    N/A
                
        size (``int`` ``64-bit``):
                    N/A
                
        mime_type (``str``):
                    N/A
                
    Returns:
        :obj:`Document<typegram.api.ayiin.Document>`
    """

    __slots__: List[str] = ["sha256", "size", "mime_type"]

    ID = 0xb1f2061f
    QUALNAME = "functions.functions.Document"

    def __init__(self, *, sha256: bytes, size: int, mime_type: str) -> None:
        
                self.sha256 = sha256  # bytes
        
                self.size = size  # long
        
                self.mime_type = mime_type  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDocumentByHash":
        # No flags
        
        sha256 = Bytes.read(b)
        
        size = Long.read(b)
        
        mime_type = String.read(b)
        
        return GetDocumentByHash(sha256=sha256, size=size, mime_type=mime_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.sha256))
        
        b.write(Long(self.size))
        
        b.write(String(self.mime_type))
        
        return b.getvalue()