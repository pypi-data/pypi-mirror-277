
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



class UploadProfilePhoto(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``388A3B5``

fallback (``bool``, *optional*):
                    N/A
                
        bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`, *optional*):
                    N/A
                
        file (:obj:`InputFile<typegram.api.ayiin.InputFile>`, *optional*):
                    N/A
                
        video (:obj:`InputFile<typegram.api.ayiin.InputFile>`, *optional*):
                    N/A
                
        video_start_ts (``float`` ``64-bit``, *optional*):
                    N/A
                
        video_emoji_markup (:obj:`VideoSize<typegram.api.ayiin.VideoSize>`, *optional*):
                    N/A
                
    Returns:
        :obj:`photos.Photo<typegram.api.ayiin.photos.Photo>`
    """

    __slots__: List[str] = ["fallback", "bot", "file", "video", "video_start_ts", "video_emoji_markup"]

    ID = 0x388a3b5
    QUALNAME = "functions.functionsphotos.Photo"

    def __init__(self, *, fallback: Optional[bool] = None, bot: "ayiin.InputUser" = None, file: "ayiin.InputFile" = None, video: "ayiin.InputFile" = None, video_start_ts: Optional[float] = None, video_emoji_markup: "ayiin.VideoSize" = None) -> None:
        
                self.fallback = fallback  # true
        
                self.bot = bot  # InputUser
        
                self.file = file  # InputFile
        
                self.video = video  # InputFile
        
                self.video_start_ts = video_start_ts  # double
        
                self.video_emoji_markup = video_emoji_markup  # VideoSize

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadProfilePhoto":
        
        flags = Int.read(b)
        
        fallback = True if flags & (1 << 3) else False
        bot = Object.read(b) if flags & (1 << 5) else None
        
        file = Object.read(b) if flags & (1 << 0) else None
        
        video = Object.read(b) if flags & (1 << 1) else None
        
        video_start_ts = Double.read(b) if flags & (1 << 2) else None
        video_emoji_markup = Object.read(b) if flags & (1 << 4) else None
        
        return UploadProfilePhoto(fallback=fallback, bot=bot, file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(self.bot.write())
        
        if self.file is not None:
            b.write(self.file.write())
        
        if self.video is not None:
            b.write(self.video.write())
        
        if self.video_start_ts is not None:
            b.write(Double(self.video_start_ts))
        
        if self.video_emoji_markup is not None:
            b.write(self.video_emoji_markup.write())
        
        return b.getvalue()