
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



class UpdateMoveStickerSetToTop(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``86FCCF85``

stickerset (``int`` ``64-bit``):
                    N/A
                
        masks (``bool``, *optional*):
                    N/A
                
        emojis (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["stickerset", "masks", "emojis"]

    ID = 0x86fccf85
    QUALNAME = "types.updateMoveStickerSetToTop"

    def __init__(self, *, stickerset: int, masks: Optional[bool] = None, emojis: Optional[bool] = None) -> None:
        
                self.stickerset = stickerset  # long
        
                self.masks = masks  # true
        
                self.emojis = emojis  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMoveStickerSetToTop":
        
        flags = Int.read(b)
        
        masks = True if flags & (1 << 0) else False
        emojis = True if flags & (1 << 1) else False
        stickerset = Long.read(b)
        
        return UpdateMoveStickerSetToTop(stickerset=stickerset, masks=masks, emojis=emojis)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.stickerset))
        
        return b.getvalue()