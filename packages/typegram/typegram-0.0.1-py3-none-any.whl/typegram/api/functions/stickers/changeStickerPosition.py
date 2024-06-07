
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



class ChangeStickerPosition(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``FFB6D4CA``

sticker (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`):
                    N/A
                
        position (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.StickerSet<typegram.api.ayiin.messages.StickerSet>`
    """

    __slots__: List[str] = ["sticker", "position"]

    ID = 0xffb6d4ca
    QUALNAME = "functions.functionsmessages.StickerSet"

    def __init__(self, *, sticker: "ayiin.InputDocument", position: int) -> None:
        
                self.sticker = sticker  # InputDocument
        
                self.position = position  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChangeStickerPosition":
        # No flags
        
        sticker = Object.read(b)
        
        position = Int.read(b)
        
        return ChangeStickerPosition(sticker=sticker, position=position)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.sticker.write())
        
        b.write(Int(self.position))
        
        return b.getvalue()