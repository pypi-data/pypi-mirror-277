
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



class TextPhone(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RichText`.

    Details:
        - Layer: ``181``
        - ID: ``1CCB966A``

text (:obj:`RichText<typegram.api.ayiin.RichText>`):
                    N/A
                
        phone (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["text", "phone"]

    ID = 0x1ccb966a
    QUALNAME = "types.textPhone"

    def __init__(self, *, text: "api.ayiin.RichText", phone: str) -> None:
        
                self.text = text  # RichText
        
                self.phone = phone  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextPhone":
        # No flags
        
        text = Object.read(b)
        
        phone = String.read(b)
        
        return TextPhone(text=text, phone=phone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(String(self.phone))
        
        return b.getvalue()