
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



class UpdateNewStickerSet(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``688A30AA``

stickerset (:obj:`messages.StickerSet<typegram.api.ayiin.messages.StickerSet>`):
                    N/A
                
    """

    __slots__: List[str] = ["stickerset"]

    ID = 0x688a30aa
    QUALNAME = "types.updateNewStickerSet"

    def __init__(self, *, stickerset: "api.ayiinmessages.StickerSet") -> None:
        
                self.stickerset = stickerset  # messages.StickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewStickerSet":
        # No flags
        
        stickerset = Object.read(b)
        
        return UpdateNewStickerSet(stickerset=stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stickerset.write())
        
        return b.getvalue()