
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



class WebPageNotModified(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WebPage`.

    Details:
        - Layer: ``181``
        - ID: ``7311CA11``

cached_page_views (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["cached_page_views"]

    ID = 0x7311ca11
    QUALNAME = "types.webPageNotModified"

    def __init__(self, *, cached_page_views: Optional[int] = None) -> None:
        
                self.cached_page_views = cached_page_views  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageNotModified":
        
        flags = Int.read(b)
        
        cached_page_views = Int.read(b) if flags & (1 << 0) else None
        return WebPageNotModified(cached_page_views=cached_page_views)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.cached_page_views is not None:
            b.write(Int(self.cached_page_views))
        
        return b.getvalue()