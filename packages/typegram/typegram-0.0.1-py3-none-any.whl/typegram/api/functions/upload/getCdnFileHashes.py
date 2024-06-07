
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



class GetCdnFileHashes(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``91DC3F31``

file_token (``bytes``):
                    N/A
                
        offset (``int`` ``64-bit``):
                    N/A
                
    Returns:
        List of :obj:`FileHash<typegram.api.ayiin.FileHash>`
    """

    __slots__: List[str] = ["file_token", "offset"]

    ID = 0x91dc3f31
    QUALNAME = "functions.functions.Vector<FileHash>"

    def __init__(self, *, file_token: bytes, offset: int) -> None:
        
                self.file_token = file_token  # bytes
        
                self.offset = offset  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCdnFileHashes":
        # No flags
        
        file_token = Bytes.read(b)
        
        offset = Long.read(b)
        
        return GetCdnFileHashes(file_token=file_token, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.file_token))
        
        b.write(Long(self.offset))
        
        return b.getvalue()