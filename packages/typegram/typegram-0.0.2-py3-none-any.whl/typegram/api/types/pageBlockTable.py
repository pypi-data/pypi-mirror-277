
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



class PageBlockTable(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PageBlock`.

    Details:
        - Layer: ``181``
        - ID: ``BF4DEA82``

title (:obj:`RichText<typegram.api.ayiin.RichText>`):
                    N/A
                
        rows (List of :obj:`PageTableRow<typegram.api.ayiin.PageTableRow>`):
                    N/A
                
        bordered (``bool``, *optional*):
                    N/A
                
        striped (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["title", "rows", "bordered", "striped"]

    ID = 0xbf4dea82
    QUALNAME = "types.pageBlockTable"

    def __init__(self, *, title: "api.ayiin.RichText", rows: List["api.ayiin.PageTableRow"], bordered: Optional[bool] = None, striped: Optional[bool] = None) -> None:
        
                self.title = title  # RichText
        
                self.rows = rows  # PageTableRow
        
                self.bordered = bordered  # true
        
                self.striped = striped  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockTable":
        
        flags = Int.read(b)
        
        bordered = True if flags & (1 << 0) else False
        striped = True if flags & (1 << 1) else False
        title = Object.read(b)
        
        rows = Object.read(b)
        
        return PageBlockTable(title=title, rows=rows, bordered=bordered, striped=striped)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.title.write())
        
        b.write(Vector(self.rows))
        
        return b.getvalue()