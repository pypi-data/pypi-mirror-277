
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



class UploadWallPaper(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E39A8F03``

file (:obj:`InputFile<typegram.api.ayiin.InputFile>`):
                    N/A
                
        mime_type (``str``):
                    N/A
                
        settings (:obj:`WallPaperSettings<typegram.api.ayiin.WallPaperSettings>`):
                    N/A
                
        for_chat (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`WallPaper<typegram.api.ayiin.WallPaper>`
    """

    __slots__: List[str] = ["file", "mime_type", "settings", "for_chat"]

    ID = 0xe39a8f03
    QUALNAME = "functions.functions.WallPaper"

    def __init__(self, *, file: "ayiin.InputFile", mime_type: str, settings: "ayiin.WallPaperSettings", for_chat: Optional[bool] = None) -> None:
        
                self.file = file  # InputFile
        
                self.mime_type = mime_type  # string
        
                self.settings = settings  # WallPaperSettings
        
                self.for_chat = for_chat  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadWallPaper":
        
        flags = Int.read(b)
        
        for_chat = True if flags & (1 << 0) else False
        file = Object.read(b)
        
        mime_type = String.read(b)
        
        settings = Object.read(b)
        
        return UploadWallPaper(file=file, mime_type=mime_type, settings=settings, for_chat=for_chat)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.file.write())
        
        b.write(String(self.mime_type))
        
        b.write(self.settings.write())
        
        return b.getvalue()