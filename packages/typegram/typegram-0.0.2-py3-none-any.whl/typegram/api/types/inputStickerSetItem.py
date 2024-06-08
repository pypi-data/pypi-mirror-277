
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



class InputStickerSetItem(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputStickerSetItem`.

    Details:
        - Layer: ``181``
        - ID: ``32DA9E9C``

document (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`):
                    N/A
                
        emoji (``str``):
                    N/A
                
        mask_coords (:obj:`MaskCoords<typegram.api.ayiin.MaskCoords>`, *optional*):
                    N/A
                
        keywords (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["document", "emoji", "mask_coords", "keywords"]

    ID = 0x32da9e9c
    QUALNAME = "types.inputStickerSetItem"

    def __init__(self, *, document: "api.ayiin.InputDocument", emoji: str, mask_coords: "api.ayiin.MaskCoords" = None, keywords: Optional[str] = None) -> None:
        
                self.document = document  # InputDocument
        
                self.emoji = emoji  # string
        
                self.mask_coords = mask_coords  # MaskCoords
        
                self.keywords = keywords  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetItem":
        
        flags = Int.read(b)
        
        document = Object.read(b)
        
        emoji = String.read(b)
        
        mask_coords = Object.read(b) if flags & (1 << 0) else None
        
        keywords = String.read(b) if flags & (1 << 1) else None
        return InputStickerSetItem(document=document, emoji=emoji, mask_coords=mask_coords, keywords=keywords)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.document.write())
        
        b.write(String(self.emoji))
        
        if self.mask_coords is not None:
            b.write(self.mask_coords.write())
        
        if self.keywords is not None:
            b.write(String(self.keywords))
        
        return b.getvalue()