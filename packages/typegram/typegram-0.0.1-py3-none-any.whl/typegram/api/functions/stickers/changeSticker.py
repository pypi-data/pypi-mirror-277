
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



class ChangeSticker(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F5537EBC``

sticker (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`):
                    N/A
                
        emoji (``str``, *optional*):
                    N/A
                
        mask_coords (:obj:`MaskCoords<typegram.api.ayiin.MaskCoords>`, *optional*):
                    N/A
                
        keywords (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.StickerSet<typegram.api.ayiin.messages.StickerSet>`
    """

    __slots__: List[str] = ["sticker", "emoji", "mask_coords", "keywords"]

    ID = 0xf5537ebc
    QUALNAME = "functions.functionsmessages.StickerSet"

    def __init__(self, *, sticker: "ayiin.InputDocument", emoji: Optional[str] = None, mask_coords: "ayiin.MaskCoords" = None, keywords: Optional[str] = None) -> None:
        
                self.sticker = sticker  # InputDocument
        
                self.emoji = emoji  # string
        
                self.mask_coords = mask_coords  # MaskCoords
        
                self.keywords = keywords  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChangeSticker":
        
        flags = Int.read(b)
        
        sticker = Object.read(b)
        
        emoji = String.read(b) if flags & (1 << 0) else None
        mask_coords = Object.read(b) if flags & (1 << 1) else None
        
        keywords = String.read(b) if flags & (1 << 2) else None
        return ChangeSticker(sticker=sticker, emoji=emoji, mask_coords=mask_coords, keywords=keywords)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.sticker.write())
        
        if self.emoji is not None:
            b.write(String(self.emoji))
        
        if self.mask_coords is not None:
            b.write(self.mask_coords.write())
        
        if self.keywords is not None:
            b.write(String(self.keywords))
        
        return b.getvalue()