
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



class InputMediaUploadedDocument(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputMedia`.

    Details:
        - Layer: ``181``
        - ID: ``5B38C6C1``

file (:obj:`InputFile<typegram.api.ayiin.InputFile>`):
                    N/A
                
        mime_type (``str``):
                    N/A
                
        attributes (List of :obj:`DocumentAttribute<typegram.api.ayiin.DocumentAttribute>`):
                    N/A
                
        nosound_video (``bool``, *optional*):
                    N/A
                
        force_file (``bool``, *optional*):
                    N/A
                
        spoiler (``bool``, *optional*):
                    N/A
                
        thumb (:obj:`InputFile<typegram.api.ayiin.InputFile>`, *optional*):
                    N/A
                
        stickers (List of :obj:`InputDocument<typegram.api.ayiin.InputDocument>`, *optional*):
                    N/A
                
        ttl_seconds (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["file", "mime_type", "attributes", "nosound_video", "force_file", "spoiler", "thumb", "stickers", "ttl_seconds"]

    ID = 0x5b38c6c1
    QUALNAME = "types.inputMediaUploadedDocument"

    def __init__(self, *, file: "api.ayiin.InputFile", mime_type: str, attributes: List["api.ayiin.DocumentAttribute"], nosound_video: Optional[bool] = None, force_file: Optional[bool] = None, spoiler: Optional[bool] = None, thumb: "api.ayiin.InputFile" = None, stickers: Optional[List["api.ayiin.InputDocument"]] = None, ttl_seconds: Optional[int] = None) -> None:
        
                self.file = file  # InputFile
        
                self.mime_type = mime_type  # string
        
                self.attributes = attributes  # DocumentAttribute
        
                self.nosound_video = nosound_video  # true
        
                self.force_file = force_file  # true
        
                self.spoiler = spoiler  # true
        
                self.thumb = thumb  # InputFile
        
                self.stickers = stickers  # InputDocument
        
                self.ttl_seconds = ttl_seconds  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaUploadedDocument":
        
        flags = Int.read(b)
        
        nosound_video = True if flags & (1 << 3) else False
        force_file = True if flags & (1 << 4) else False
        spoiler = True if flags & (1 << 5) else False
        file = Object.read(b)
        
        thumb = Object.read(b) if flags & (1 << 2) else None
        
        mime_type = String.read(b)
        
        attributes = Object.read(b)
        
        stickers = Object.read(b) if flags & (1 << 0) else []
        
        ttl_seconds = Int.read(b) if flags & (1 << 1) else None
        return InputMediaUploadedDocument(file=file, mime_type=mime_type, attributes=attributes, nosound_video=nosound_video, force_file=force_file, spoiler=spoiler, thumb=thumb, stickers=stickers, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.file.write())
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        b.write(String(self.mime_type))
        
        b.write(Vector(self.attributes))
        
        if self.stickers is not None:
            b.write(Vector(self.stickers))
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        return b.getvalue()