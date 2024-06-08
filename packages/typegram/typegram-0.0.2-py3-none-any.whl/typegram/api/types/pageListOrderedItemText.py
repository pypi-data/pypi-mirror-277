
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



class PageListOrderedItemText(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PageListOrderedItem`.

    Details:
        - Layer: ``181``
        - ID: ``5E068047``

num (``str``):
                    N/A
                
        text (:obj:`RichText<typegram.api.ayiin.RichText>`):
                    N/A
                
    """

    __slots__: List[str] = ["num", "text"]

    ID = 0x5e068047
    QUALNAME = "types.pageListOrderedItemText"

    def __init__(self, *, num: str, text: "api.ayiin.RichText") -> None:
        
                self.num = num  # string
        
                self.text = text  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageListOrderedItemText":
        # No flags
        
        num = String.read(b)
        
        text = Object.read(b)
        
        return PageListOrderedItemText(num=num, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.num))
        
        b.write(self.text.write())
        
        return b.getvalue()