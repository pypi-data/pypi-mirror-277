
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



class VideoSizeEmojiMarkup(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.VideoSize`.

    Details:
        - Layer: ``181``
        - ID: ``F85C413C``

emoji_id (``int`` ``64-bit``):
                    N/A
                
        background_colors (List of ``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["emoji_id", "background_colors"]

    ID = 0xf85c413c
    QUALNAME = "types.videoSizeEmojiMarkup"

    def __init__(self, *, emoji_id: int, background_colors: List[int]) -> None:
        
                self.emoji_id = emoji_id  # long
        
                self.background_colors = background_colors  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VideoSizeEmojiMarkup":
        # No flags
        
        emoji_id = Long.read(b)
        
        background_colors = Object.read(b, Int)
        
        return VideoSizeEmojiMarkup(emoji_id=emoji_id, background_colors=background_colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.emoji_id))
        
        b.write(Vector(self.background_colors, Int))
        
        return b.getvalue()