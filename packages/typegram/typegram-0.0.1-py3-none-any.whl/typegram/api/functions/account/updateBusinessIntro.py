
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

from typegram.api import ayiin, functions
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class UpdateBusinessIntro(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A614D034``

intro (:obj:`InputBusinessIntro<typegram.api.ayiin.InputBusinessIntro>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["intro"]

    ID = 0xa614d034
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, intro: "ayiin.InputBusinessIntro" = None) -> None:
        
                self.intro = intro  # InputBusinessIntro

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessIntro":
        
        flags = Int.read(b)
        
        intro = Object.read(b) if flags & (1 << 0) else None
        
        return UpdateBusinessIntro(intro=intro)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.intro is not None:
            b.write(self.intro.write())
        
        return b.getvalue()