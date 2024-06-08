
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



class PhotoStrippedSize(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PhotoSize`.

    Details:
        - Layer: ``181``
        - ID: ``E0B0BC2E``

type (``str``):
                    N/A
                
        bytes (``bytes``):
                    N/A
                
    """

    __slots__: List[str] = ["type", "bytes"]

    ID = 0xe0b0bc2e
    QUALNAME = "types.photoStrippedSize"

    def __init__(self, *, type: str, bytes: bytes) -> None:
        
                self.type = type  # string
        
                self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotoStrippedSize":
        # No flags
        
        type = String.read(b)
        
        bytes = Bytes.read(b)
        
        return PhotoStrippedSize(type=type, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.type))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()