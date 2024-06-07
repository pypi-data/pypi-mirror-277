
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



class GetFileHashes(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9156982A``

location (:obj:`InputFileLocation<typegram.api.ayiin.InputFileLocation>`):
                    N/A
                
        offset (``int`` ``64-bit``):
                    N/A
                
    Returns:
        List of :obj:`FileHash<typegram.api.ayiin.FileHash>`
    """

    __slots__: List[str] = ["location", "offset"]

    ID = 0x9156982a
    QUALNAME = "functions.functions.Vector<FileHash>"

    def __init__(self, *, location: "ayiin.InputFileLocation", offset: int) -> None:
        
                self.location = location  # InputFileLocation
        
                self.offset = offset  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFileHashes":
        # No flags
        
        location = Object.read(b)
        
        offset = Long.read(b)
        
        return GetFileHashes(location=location, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.location.write())
        
        b.write(Long(self.offset))
        
        return b.getvalue()