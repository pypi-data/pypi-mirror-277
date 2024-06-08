
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



class MessageExtendedMediaPreview(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageExtendedMedia`.

    Details:
        - Layer: ``181``
        - ID: ``AD628CC8``

w (``int`` ``32-bit``, *optional*):
                    N/A
                
        h (``int`` ``32-bit``, *optional*):
                    N/A
                
        thumb (:obj:`PhotoSize<typegram.api.ayiin.PhotoSize>`, *optional*):
                    N/A
                
        video_duration (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["w", "h", "thumb", "video_duration"]

    ID = 0xad628cc8
    QUALNAME = "types.messageExtendedMediaPreview"

    def __init__(self, *, w: Optional[int] = None, h: Optional[int] = None, thumb: "api.ayiin.PhotoSize" = None, video_duration: Optional[int] = None) -> None:
        
                self.w = w  # int
        
                self.h = h  # int
        
                self.thumb = thumb  # PhotoSize
        
                self.video_duration = video_duration  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageExtendedMediaPreview":
        
        flags = Int.read(b)
        
        w = Int.read(b) if flags & (1 << 0) else None
        h = Int.read(b) if flags & (1 << 0) else None
        thumb = Object.read(b) if flags & (1 << 1) else None
        
        video_duration = Int.read(b) if flags & (1 << 2) else None
        return MessageExtendedMediaPreview(w=w, h=h, thumb=thumb, video_duration=video_duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.w is not None:
            b.write(Int(self.w))
        
        if self.h is not None:
            b.write(Int(self.h))
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        if self.video_duration is not None:
            b.write(Int(self.video_duration))
        
        return b.getvalue()