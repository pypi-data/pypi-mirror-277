
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



class TextAnchor(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RichText`.

    Details:
        - Layer: ``181``
        - ID: ``35553762``

text (:obj:`RichText<typegram.api.ayiin.RichText>`):
                    N/A
                
        name (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["text", "name"]

    ID = 0x35553762
    QUALNAME = "types.textAnchor"

    def __init__(self, *, text: "api.ayiin.RichText", name: str) -> None:
        
                self.text = text  # RichText
        
                self.name = name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextAnchor":
        # No flags
        
        text = Object.read(b)
        
        name = String.read(b)
        
        return TextAnchor(text=text, name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(String(self.name))
        
        return b.getvalue()