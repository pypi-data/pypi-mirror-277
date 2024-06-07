
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



class ReplaceSticker(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``4696459A``

sticker (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`):
                    N/A
                
        new_sticker (:obj:`InputStickerSetItem<typegram.api.ayiin.InputStickerSetItem>`):
                    N/A
                
    Returns:
        :obj:`messages.StickerSet<typegram.api.ayiin.messages.StickerSet>`
    """

    __slots__: List[str] = ["sticker", "new_sticker"]

    ID = 0x4696459a
    QUALNAME = "functions.functionsmessages.StickerSet"

    def __init__(self, *, sticker: "ayiin.InputDocument", new_sticker: "ayiin.InputStickerSetItem") -> None:
        
                self.sticker = sticker  # InputDocument
        
                self.new_sticker = new_sticker  # InputStickerSetItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplaceSticker":
        # No flags
        
        sticker = Object.read(b)
        
        new_sticker = Object.read(b)
        
        return ReplaceSticker(sticker=sticker, new_sticker=new_sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.sticker.write())
        
        b.write(self.new_sticker.write())
        
        return b.getvalue()