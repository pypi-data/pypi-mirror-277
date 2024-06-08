
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



class InputBusinessIntro(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBusinessIntro`.

    Details:
        - Layer: ``181``
        - ID: ``9C469CD``

title (``str``):
                    N/A
                
        description (``str``):
                    N/A
                
        sticker (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["title", "description", "sticker"]

    ID = 0x9c469cd
    QUALNAME = "types.inputBusinessIntro"

    def __init__(self, *, title: str, description: str, sticker: "api.ayiin.InputDocument" = None) -> None:
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.sticker = sticker  # InputDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBusinessIntro":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        sticker = Object.read(b) if flags & (1 << 0) else None
        
        return InputBusinessIntro(title=title, description=description, sticker=sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.sticker is not None:
            b.write(self.sticker.write())
        
        return b.getvalue()