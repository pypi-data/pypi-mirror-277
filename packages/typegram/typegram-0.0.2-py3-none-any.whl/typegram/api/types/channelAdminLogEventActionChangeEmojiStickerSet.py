
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



class ChannelAdminLogEventActionChangeEmojiStickerSet(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``181``
        - ID: ``46D840AB``

prev_stickerset (:obj:`InputStickerSet<typegram.api.ayiin.InputStickerSet>`):
                    N/A
                
        new_stickerset (:obj:`InputStickerSet<typegram.api.ayiin.InputStickerSet>`):
                    N/A
                
    """

    __slots__: List[str] = ["prev_stickerset", "new_stickerset"]

    ID = 0x46d840ab
    QUALNAME = "types.channelAdminLogEventActionChangeEmojiStickerSet"

    def __init__(self, *, prev_stickerset: "api.ayiin.InputStickerSet", new_stickerset: "api.ayiin.InputStickerSet") -> None:
        
                self.prev_stickerset = prev_stickerset  # InputStickerSet
        
                self.new_stickerset = new_stickerset  # InputStickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeEmojiStickerSet":
        # No flags
        
        prev_stickerset = Object.read(b)
        
        new_stickerset = Object.read(b)
        
        return ChannelAdminLogEventActionChangeEmojiStickerSet(prev_stickerset=prev_stickerset, new_stickerset=new_stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_stickerset.write())
        
        b.write(self.new_stickerset.write())
        
        return b.getvalue()