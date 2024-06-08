
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



class PageCaption(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PageCaption`.

    Details:
        - Layer: ``181``
        - ID: ``6F747657``

text (:obj:`RichText<typegram.api.ayiin.RichText>`):
                    N/A
                
        credit (:obj:`RichText<typegram.api.ayiin.RichText>`):
                    N/A
                
    """

    __slots__: List[str] = ["text", "credit"]

    ID = 0x6f747657
    QUALNAME = "types.pageCaption"

    def __init__(self, *, text: "api.ayiin.RichText", credit: "api.ayiin.RichText") -> None:
        
                self.text = text  # RichText
        
                self.credit = credit  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageCaption":
        # No flags
        
        text = Object.read(b)
        
        credit = Object.read(b)
        
        return PageCaption(text=text, credit=credit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(self.credit.write())
        
        return b.getvalue()