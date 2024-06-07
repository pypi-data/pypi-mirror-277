
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



class ToggleGroupCallRecord(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F128C708``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        start (``bool``, *optional*):
                    N/A
                
        video (``bool``, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        video_portrait (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["call", "start", "video", "title", "video_portrait"]

    ID = 0xf128c708
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, call: "ayiin.InputGroupCall", start: Optional[bool] = None, video: Optional[bool] = None, title: Optional[str] = None, video_portrait: Optional[bool] = None) -> None:
        
                self.call = call  # InputGroupCall
        
                self.start = start  # true
        
                self.video = video  # true
        
                self.title = title  # string
        
                self.video_portrait = video_portrait  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleGroupCallRecord":
        
        flags = Int.read(b)
        
        start = True if flags & (1 << 0) else False
        video = True if flags & (1 << 2) else False
        call = Object.read(b)
        
        title = String.read(b) if flags & (1 << 1) else None
        video_portrait = Bool.read(b) if flags & (1 << 2) else None
        return ToggleGroupCallRecord(call=call, start=start, video=video, title=title, video_portrait=video_portrait)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.video_portrait is not None:
            b.write(Bool(self.video_portrait))
        
        return b.getvalue()