
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



class UploadTheme(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``1C3DB333``

file (:obj:`InputFile<typegram.api.ayiin.InputFile>`):
                    N/A
                
        file_name (``str``):
                    N/A
                
        mime_type (``str``):
                    N/A
                
        thumb (:obj:`InputFile<typegram.api.ayiin.InputFile>`, *optional*):
                    N/A
                
    Returns:
        :obj:`Document<typegram.api.ayiin.Document>`
    """

    __slots__: List[str] = ["file", "file_name", "mime_type", "thumb"]

    ID = 0x1c3db333
    QUALNAME = "functions.functions.Document"

    def __init__(self, *, file: "ayiin.InputFile", file_name: str, mime_type: str, thumb: "ayiin.InputFile" = None) -> None:
        
                self.file = file  # InputFile
        
                self.file_name = file_name  # string
        
                self.mime_type = mime_type  # string
        
                self.thumb = thumb  # InputFile

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadTheme":
        
        flags = Int.read(b)
        
        file = Object.read(b)
        
        thumb = Object.read(b) if flags & (1 << 0) else None
        
        file_name = String.read(b)
        
        mime_type = String.read(b)
        
        return UploadTheme(file=file, file_name=file_name, mime_type=mime_type, thumb=thumb)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.file.write())
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        b.write(String(self.file_name))
        
        b.write(String(self.mime_type))
        
        return b.getvalue()