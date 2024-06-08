
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



class InlineBotWebView(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InlineBotWebView`.

    Details:
        - Layer: ``181``
        - ID: ``B57295D5``

text (``str``):
                    N/A
                
        url (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["text", "url"]

    ID = 0xb57295d5
    QUALNAME = "types.inlineBotWebView"

    def __init__(self, *, text: str, url: str) -> None:
        
                self.text = text  # string
        
                self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InlineBotWebView":
        # No flags
        
        text = String.read(b)
        
        url = String.read(b)
        
        return InlineBotWebView(text=text, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(String(self.url))
        
        return b.getvalue()