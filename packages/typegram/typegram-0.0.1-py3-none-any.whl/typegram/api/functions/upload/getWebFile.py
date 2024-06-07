
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



class GetWebFile(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``24E6818D``

location (:obj:`InputWebFileLocation<typegram.api.ayiin.InputWebFileLocation>`):
                    N/A
                
        offset (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`upload.WebFile<typegram.api.ayiin.upload.WebFile>`
    """

    __slots__: List[str] = ["location", "offset", "limit"]

    ID = 0x24e6818d
    QUALNAME = "functions.functionsupload.WebFile"

    def __init__(self, *, location: "ayiin.InputWebFileLocation", offset: int, limit: int) -> None:
        
                self.location = location  # InputWebFileLocation
        
                self.offset = offset  # int
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWebFile":
        # No flags
        
        location = Object.read(b)
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        return GetWebFile(location=location, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.location.write())
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()