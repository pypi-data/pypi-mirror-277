
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



class InputChatUploadedPhoto(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputChatPhoto`.

    Details:
        - Layer: ``181``
        - ID: ``BDCDAEC0``

file (:obj:`InputFile<typegram.api.ayiin.InputFile>`, *optional*):
                    N/A
                
        video (:obj:`InputFile<typegram.api.ayiin.InputFile>`, *optional*):
                    N/A
                
        video_start_ts (``float`` ``64-bit``, *optional*):
                    N/A
                
        video_emoji_markup (:obj:`VideoSize<typegram.api.ayiin.VideoSize>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["file", "video", "video_start_ts", "video_emoji_markup"]

    ID = 0xbdcdaec0
    QUALNAME = "types.inputChatUploadedPhoto"

    def __init__(self, *, file: "api.ayiin.InputFile" = None, video: "api.ayiin.InputFile" = None, video_start_ts: Optional[float] = None, video_emoji_markup: "api.ayiin.VideoSize" = None) -> None:
        
                self.file = file  # InputFile
        
                self.video = video  # InputFile
        
                self.video_start_ts = video_start_ts  # double
        
                self.video_emoji_markup = video_emoji_markup  # VideoSize

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChatUploadedPhoto":
        
        flags = Int.read(b)
        
        file = Object.read(b) if flags & (1 << 0) else None
        
        video = Object.read(b) if flags & (1 << 1) else None
        
        video_start_ts = Double.read(b) if flags & (1 << 2) else None
        video_emoji_markup = Object.read(b) if flags & (1 << 3) else None
        
        return InputChatUploadedPhoto(file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.file is not None:
            b.write(self.file.write())
        
        if self.video is not None:
            b.write(self.video.write())
        
        if self.video_start_ts is not None:
            b.write(Double(self.video_start_ts))
        
        if self.video_emoji_markup is not None:
            b.write(self.video_emoji_markup.write())
        
        return b.getvalue()