
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



class PageBlockOrderedList(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PageBlock`.

    Details:
        - Layer: ``181``
        - ID: ``9A8AE1E1``

items (List of :obj:`PageListOrderedItem<typegram.api.ayiin.PageListOrderedItem>`):
                    N/A
                
    """

    __slots__: List[str] = ["items"]

    ID = 0x9a8ae1e1
    QUALNAME = "types.pageBlockOrderedList"

    def __init__(self, *, items: List["api.ayiin.PageListOrderedItem"]) -> None:
        
                self.items = items  # PageListOrderedItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockOrderedList":
        # No flags
        
        items = Object.read(b)
        
        return PageBlockOrderedList(items=items)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.items))
        
        return b.getvalue()