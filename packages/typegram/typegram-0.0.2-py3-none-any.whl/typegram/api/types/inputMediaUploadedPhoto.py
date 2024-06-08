
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



class InputMediaUploadedPhoto(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputMedia`.

    Details:
        - Layer: ``181``
        - ID: ``1E287D04``

file (:obj:`InputFile<typegram.api.ayiin.InputFile>`):
                    N/A
                
        spoiler (``bool``, *optional*):
                    N/A
                
        stickers (List of :obj:`InputDocument<typegram.api.ayiin.InputDocument>`, *optional*):
                    N/A
                
        ttl_seconds (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["file", "spoiler", "stickers", "ttl_seconds"]

    ID = 0x1e287d04
    QUALNAME = "types.inputMediaUploadedPhoto"

    def __init__(self, *, file: "api.ayiin.InputFile", spoiler: Optional[bool] = None, stickers: Optional[List["api.ayiin.InputDocument"]] = None, ttl_seconds: Optional[int] = None) -> None:
        
                self.file = file  # InputFile
        
                self.spoiler = spoiler  # true
        
                self.stickers = stickers  # InputDocument
        
                self.ttl_seconds = ttl_seconds  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaUploadedPhoto":
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 2) else False
        file = Object.read(b)
        
        stickers = Object.read(b) if flags & (1 << 0) else []
        
        ttl_seconds = Int.read(b) if flags & (1 << 1) else None
        return InputMediaUploadedPhoto(file=file, spoiler=spoiler, stickers=stickers, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.file.write())
        
        if self.stickers is not None:
            b.write(Vector(self.stickers))
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        return b.getvalue()