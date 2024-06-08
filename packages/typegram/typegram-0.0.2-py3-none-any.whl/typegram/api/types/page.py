
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



class Page(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Page`.

    Details:
        - Layer: ``181``
        - ID: ``98657F0D``

url (``str``):
                    N/A
                
        blocks (List of :obj:`PageBlock<typegram.api.ayiin.PageBlock>`):
                    N/A
                
        photos (List of :obj:`Photo<typegram.api.ayiin.Photo>`):
                    N/A
                
        documents (List of :obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
        part (``bool``, *optional*):
                    N/A
                
        rtl (``bool``, *optional*):
                    N/A
                
        v2 (``bool``, *optional*):
                    N/A
                
        views (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["url", "blocks", "photos", "documents", "part", "rtl", "v2", "views"]

    ID = 0x98657f0d
    QUALNAME = "types.page"

    def __init__(self, *, url: str, blocks: List["api.ayiin.PageBlock"], photos: List["api.ayiin.Photo"], documents: List["api.ayiin.Document"], part: Optional[bool] = None, rtl: Optional[bool] = None, v2: Optional[bool] = None, views: Optional[int] = None) -> None:
        
                self.url = url  # string
        
                self.blocks = blocks  # PageBlock
        
                self.photos = photos  # Photo
        
                self.documents = documents  # Document
        
                self.part = part  # true
        
                self.rtl = rtl  # true
        
                self.v2 = v2  # true
        
                self.views = views  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Page":
        
        flags = Int.read(b)
        
        part = True if flags & (1 << 0) else False
        rtl = True if flags & (1 << 1) else False
        v2 = True if flags & (1 << 2) else False
        url = String.read(b)
        
        blocks = Object.read(b)
        
        photos = Object.read(b)
        
        documents = Object.read(b)
        
        views = Int.read(b) if flags & (1 << 3) else None
        return Page(url=url, blocks=blocks, photos=photos, documents=documents, part=part, rtl=rtl, v2=v2, views=views)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.url))
        
        b.write(Vector(self.blocks))
        
        b.write(Vector(self.photos))
        
        b.write(Vector(self.documents))
        
        if self.views is not None:
            b.write(Int(self.views))
        
        return b.getvalue()