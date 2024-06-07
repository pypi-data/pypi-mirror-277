
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



class GetFile(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``BE5335BE``

location (:obj:`InputFileLocation<typegram.api.ayiin.InputFileLocation>`):
                    N/A
                
        offset (``int`` ``64-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        precise (``bool``, *optional*):
                    N/A
                
        cdn_supported (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`upload.File<typegram.api.ayiin.upload.File>`
    """

    __slots__: List[str] = ["location", "offset", "limit", "precise", "cdn_supported"]

    ID = 0xbe5335be
    QUALNAME = "functions.functionsupload.File"

    def __init__(self, *, location: "ayiin.InputFileLocation", offset: int, limit: int, precise: Optional[bool] = None, cdn_supported: Optional[bool] = None) -> None:
        
                self.location = location  # InputFileLocation
        
                self.offset = offset  # long
        
                self.limit = limit  # int
        
                self.precise = precise  # true
        
                self.cdn_supported = cdn_supported  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFile":
        
        flags = Int.read(b)
        
        precise = True if flags & (1 << 0) else False
        cdn_supported = True if flags & (1 << 1) else False
        location = Object.read(b)
        
        offset = Long.read(b)
        
        limit = Int.read(b)
        
        return GetFile(location=location, offset=offset, limit=limit, precise=precise, cdn_supported=cdn_supported)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.location.write())
        
        b.write(Long(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()