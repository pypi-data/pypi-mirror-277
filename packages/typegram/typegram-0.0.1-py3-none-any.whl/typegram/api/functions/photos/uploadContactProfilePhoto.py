
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



class UploadContactProfilePhoto(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E14C4A71``

user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        suggest (``bool``, *optional*):
                    N/A
                
        save (``bool``, *optional*):
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

    __slots__: List[str] = ["user_id", "suggest", "save", "file", "video", "video_start_ts", "video_emoji_markup"]

    ID = 0xe14c4a71
    QUALNAME = "functions.functionsphotos.Photo"

    def __init__(self, *, user_id: "ayiin.InputUser", suggest: Optional[bool] = None, save: Optional[bool] = None, file: "ayiin.InputFile" = None, video: "ayiin.InputFile" = None, video_start_ts: Optional[float] = None, video_emoji_markup: "ayiin.VideoSize" = None) -> None:
        
                self.user_id = user_id  # InputUser
        
                self.suggest = suggest  # true
        
                self.save = save  # true
        
                self.file = file  # InputFile
        
                self.video = video  # InputFile
        
                self.video_start_ts = video_start_ts  # double
        
                self.video_emoji_markup = video_emoji_markup  # VideoSize

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadContactProfilePhoto":
        
        flags = Int.read(b)
        
        suggest = True if flags & (1 << 3) else False
        save = True if flags & (1 << 4) else False
        user_id = Object.read(b)
        
        file = Object.read(b) if flags & (1 << 0) else None
        
        video = Object.read(b) if flags & (1 << 1) else None
        
        video_start_ts = Double.read(b) if flags & (1 << 2) else None
        video_emoji_markup = Object.read(b) if flags & (1 << 5) else None
        
        return UploadContactProfilePhoto(user_id=user_id, suggest=suggest, save=save, file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        if self.file is not None:
            b.write(self.file.write())
        
        if self.video is not None:
            b.write(self.video.write())
        
        if self.video_start_ts is not None:
            b.write(Double(self.video_start_ts))
        
        if self.video_emoji_markup is not None:
            b.write(self.video_emoji_markup.write())
        
        return b.getvalue()