
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



class WebPageEmpty(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WebPage`.

    Details:
        - Layer: ``181``
        - ID: ``211A1788``

id (``int`` ``64-bit``):
                    N/A
                
        url (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "url"]

    ID = 0x211a1788
    QUALNAME = "types.webPageEmpty"

    def __init__(self, *, id: int, url: Optional[str] = None) -> None:
        
                self.id = id  # long
        
                self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageEmpty":
        
        flags = Int.read(b)
        
        id = Long.read(b)
        
        url = String.read(b) if flags & (1 << 0) else None
        return WebPageEmpty(id=id, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        if self.url is not None:
            b.write(String(self.url))
        
        return b.getvalue()