
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



class PageBlockPhoto(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PageBlock`.

    Details:
        - Layer: ``181``
        - ID: ``1759C560``

photo_id (``int`` ``64-bit``):
                    N/A
                
        caption (:obj:`PageCaption<typegram.api.ayiin.PageCaption>`):
                    N/A
                
        url (``str``, *optional*):
                    N/A
                
        webpage_id (``int`` ``64-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["photo_id", "caption", "url", "webpage_id"]

    ID = 0x1759c560
    QUALNAME = "types.pageBlockPhoto"

    def __init__(self, *, photo_id: int, caption: "api.ayiin.PageCaption", url: Optional[str] = None, webpage_id: Optional[int] = None) -> None:
        
                self.photo_id = photo_id  # long
        
                self.caption = caption  # PageCaption
        
                self.url = url  # string
        
                self.webpage_id = webpage_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockPhoto":
        
        flags = Int.read(b)
        
        photo_id = Long.read(b)
        
        caption = Object.read(b)
        
        url = String.read(b) if flags & (1 << 0) else None
        webpage_id = Long.read(b) if flags & (1 << 0) else None
        return PageBlockPhoto(photo_id=photo_id, caption=caption, url=url, webpage_id=webpage_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.photo_id))
        
        b.write(self.caption.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.webpage_id is not None:
            b.write(Long(self.webpage_id))
        
        return b.getvalue()