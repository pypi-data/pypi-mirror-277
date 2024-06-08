
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



class WebPageAttributeStickerSet(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WebPageAttribute`.

    Details:
        - Layer: ``181``
        - ID: ``50CC03D3``

stickers (List of :obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
        emojis (``bool``, *optional*):
                    N/A
                
        text_color (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["stickers", "emojis", "text_color"]

    ID = 0x50cc03d3
    QUALNAME = "types.webPageAttributeStickerSet"

    def __init__(self, *, stickers: List["api.ayiin.Document"], emojis: Optional[bool] = None, text_color: Optional[bool] = None) -> None:
        
                self.stickers = stickers  # Document
        
                self.emojis = emojis  # true
        
                self.text_color = text_color  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeStickerSet":
        
        flags = Int.read(b)
        
        emojis = True if flags & (1 << 0) else False
        text_color = True if flags & (1 << 1) else False
        stickers = Object.read(b)
        
        return WebPageAttributeStickerSet(stickers=stickers, emojis=emojis, text_color=text_color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.stickers))
        
        return b.getvalue()