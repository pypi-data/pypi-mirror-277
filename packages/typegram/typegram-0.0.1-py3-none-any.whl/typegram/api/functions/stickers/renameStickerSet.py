
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



class RenameStickerSet(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``124B1C00``

stickerset (:obj:`InputStickerSet<typegram.api.ayiin.InputStickerSet>`):
                    N/A
                
        title (``str``):
                    N/A
                
    Returns:
        :obj:`messages.StickerSet<typegram.api.ayiin.messages.StickerSet>`
    """

    __slots__: List[str] = ["stickerset", "title"]

    ID = 0x124b1c00
    QUALNAME = "functions.functionsmessages.StickerSet"

    def __init__(self, *, stickerset: "ayiin.InputStickerSet", title: str) -> None:
        
                self.stickerset = stickerset  # InputStickerSet
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RenameStickerSet":
        # No flags
        
        stickerset = Object.read(b)
        
        title = String.read(b)
        
        return RenameStickerSet(stickerset=stickerset, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stickerset.write())
        
        b.write(String(self.title))
        
        return b.getvalue()