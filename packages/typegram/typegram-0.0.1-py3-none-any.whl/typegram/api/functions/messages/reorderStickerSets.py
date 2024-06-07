
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



class ReorderStickerSets(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``78337739``

order (List of ``int`` ``64-bit``):
                    N/A
                
        masks (``bool``, *optional*):
                    N/A
                
        emojis (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["order", "masks", "emojis"]

    ID = 0x78337739
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, order: List[int], masks: Optional[bool] = None, emojis: Optional[bool] = None) -> None:
        
                self.order = order  # long
        
                self.masks = masks  # true
        
                self.emojis = emojis  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderStickerSets":
        
        flags = Int.read(b)
        
        masks = True if flags & (1 << 0) else False
        emojis = True if flags & (1 << 1) else False
        order = Object.read(b, Long)
        
        return ReorderStickerSets(order=order, masks=masks, emojis=emojis)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.order, Long))
        
        return b.getvalue()