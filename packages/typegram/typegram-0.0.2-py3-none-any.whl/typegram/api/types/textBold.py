
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



class TextBold(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RichText`.

    Details:
        - Layer: ``181``
        - ID: ``6724ABC4``

text (:obj:`RichText<typegram.api.ayiin.RichText>`):
                    N/A
                
    """

    __slots__: List[str] = ["text"]

    ID = 0x6724abc4
    QUALNAME = "types.textBold"

    def __init__(self, *, text: "api.ayiin.RichText") -> None:
        
                self.text = text  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextBold":
        # No flags
        
        text = Object.read(b)
        
        return TextBold(text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        return b.getvalue()