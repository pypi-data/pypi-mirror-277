
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



class TextEmail(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RichText`.

    Details:
        - Layer: ``181``
        - ID: ``DE5A0DD6``

text (:obj:`RichText<typegram.api.ayiin.RichText>`):
                    N/A
                
        email (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["text", "email"]

    ID = 0xde5a0dd6
    QUALNAME = "types.textEmail"

    def __init__(self, *, text: "api.ayiin.RichText", email: str) -> None:
        
                self.text = text  # RichText
        
                self.email = email  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextEmail":
        # No flags
        
        text = Object.read(b)
        
        email = String.read(b)
        
        return TextEmail(text=text, email=email)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(String(self.email))
        
        return b.getvalue()