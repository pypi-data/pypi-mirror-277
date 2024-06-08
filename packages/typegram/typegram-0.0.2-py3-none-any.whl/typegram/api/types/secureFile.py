
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



class SecureFile(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SecureFile`.

    Details:
        - Layer: ``181``
        - ID: ``7D09C27E``

id (``int`` ``64-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        size (``int`` ``64-bit``):
                    N/A
                
        dc_id (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        file_hash (``bytes``):
                    N/A
                
        secret (``bytes``):
                    N/A
                
    """

    __slots__: List[str] = ["id", "access_hash", "size", "dc_id", "date", "file_hash", "secret"]

    ID = 0x7d09c27e
    QUALNAME = "types.secureFile"

    def __init__(self, *, id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: bytes, secret: bytes) -> None:
        
                self.id = id  # long
        
                self.access_hash = access_hash  # long
        
                self.size = size  # long
        
                self.dc_id = dc_id  # int
        
                self.date = date  # int
        
                self.file_hash = file_hash  # bytes
        
                self.secret = secret  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureFile":
        # No flags
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        size = Long.read(b)
        
        dc_id = Int.read(b)
        
        date = Int.read(b)
        
        file_hash = Bytes.read(b)
        
        secret = Bytes.read(b)
        
        return SecureFile(id=id, access_hash=access_hash, size=size, dc_id=dc_id, date=date, file_hash=file_hash, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Long(self.size))
        
        b.write(Int(self.dc_id))
        
        b.write(Int(self.date))
        
        b.write(Bytes(self.file_hash))
        
        b.write(Bytes(self.secret))
        
        return b.getvalue()