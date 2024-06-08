
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



class PageBlockPreformatted(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PageBlock`.

    Details:
        - Layer: ``181``
        - ID: ``C070D93E``

text (:obj:`RichText<typegram.api.ayiin.RichText>`):
                    N/A
                
        language (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["text", "language"]

    ID = 0xc070d93e
    QUALNAME = "types.pageBlockPreformatted"

    def __init__(self, *, text: "api.ayiin.RichText", language: str) -> None:
        
                self.text = text  # RichText
        
                self.language = language  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockPreformatted":
        # No flags
        
        text = Object.read(b)
        
        language = String.read(b)
        
        return PageBlockPreformatted(text=text, language=language)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(String(self.language))
        
        return b.getvalue()