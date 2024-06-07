
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



class SetEmojiStickers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3CD930B7``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        stickerset (:obj:`InputStickerSet<typegram.api.ayiin.InputStickerSet>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "stickerset"]

    ID = 0x3cd930b7
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, channel: "ayiin.InputChannel", stickerset: "ayiin.InputStickerSet") -> None:
        
                self.channel = channel  # InputChannel
        
                self.stickerset = stickerset  # InputStickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetEmojiStickers":
        # No flags
        
        channel = Object.read(b)
        
        stickerset = Object.read(b)
        
        return SetEmojiStickers(channel=channel, stickerset=stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.stickerset.write())
        
        return b.getvalue()