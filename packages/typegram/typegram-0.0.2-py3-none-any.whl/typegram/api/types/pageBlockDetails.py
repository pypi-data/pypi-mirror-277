
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



class PageBlockDetails(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PageBlock`.

    Details:
        - Layer: ``181``
        - ID: ``76768BED``

blocks (List of :obj:`PageBlock<typegram.api.ayiin.PageBlock>`):
                    N/A
                
        title (:obj:`RichText<typegram.api.ayiin.RichText>`):
                    N/A
                
        open (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["blocks", "title", "open"]

    ID = 0x76768bed
    QUALNAME = "types.pageBlockDetails"

    def __init__(self, *, blocks: List["api.ayiin.PageBlock"], title: "api.ayiin.RichText", open: Optional[bool] = None) -> None:
        
                self.blocks = blocks  # PageBlock
        
                self.title = title  # RichText
        
                self.open = open  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockDetails":
        
        flags = Int.read(b)
        
        open = True if flags & (1 << 0) else False
        blocks = Object.read(b)
        
        title = Object.read(b)
        
        return PageBlockDetails(blocks=blocks, title=title, open=open)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.blocks))
        
        b.write(self.title.write())
        
        return b.getvalue()