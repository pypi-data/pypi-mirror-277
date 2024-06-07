
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



class SaveBigFilePart(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``DE7B673D``

file_id (``int`` ``64-bit``):
                    N/A
                
        file_part (``int`` ``32-bit``):
                    N/A
                
        file_total_parts (``int`` ``32-bit``):
                    N/A
                
        bytes (``bytes``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["file_id", "file_part", "file_total_parts", "bytes"]

    ID = 0xde7b673d
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, file_id: int, file_part: int, file_total_parts: int, bytes: bytes) -> None:
        
                self.file_id = file_id  # long
        
                self.file_part = file_part  # int
        
                self.file_total_parts = file_total_parts  # int
        
                self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveBigFilePart":
        # No flags
        
        file_id = Long.read(b)
        
        file_part = Int.read(b)
        
        file_total_parts = Int.read(b)
        
        bytes = Bytes.read(b)
        
        return SaveBigFilePart(file_id=file_id, file_part=file_part, file_total_parts=file_total_parts, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.file_id))
        
        b.write(Int(self.file_part))
        
        b.write(Int(self.file_total_parts))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()