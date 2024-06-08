
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



class TextUrl(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RichText`.

    Details:
        - Layer: ``181``
        - ID: ``3C2884C1``

text (:obj:`RichText<typegram.api.ayiin.RichText>`):
                    N/A
                
        url (``str``):
                    N/A
                
        webpage_id (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["text", "url", "webpage_id"]

    ID = 0x3c2884c1
    QUALNAME = "types.textUrl"

    def __init__(self, *, text: "api.ayiin.RichText", url: str, webpage_id: int) -> None:
        
                self.text = text  # RichText
        
                self.url = url  # string
        
                self.webpage_id = webpage_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextUrl":
        # No flags
        
        text = Object.read(b)
        
        url = String.read(b)
        
        webpage_id = Long.read(b)
        
        return TextUrl(text=text, url=url, webpage_id=webpage_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(String(self.url))
        
        b.write(Long(self.webpage_id))
        
        return b.getvalue()