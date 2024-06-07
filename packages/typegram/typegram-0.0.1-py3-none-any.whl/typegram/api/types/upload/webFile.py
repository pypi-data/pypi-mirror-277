
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



class WebFile(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.upload.WebFile`.

    Details:
        - Layer: ``181``
        - ID: ``21E753BC``

size (``int`` ``32-bit``):
                    N/A
                
        mime_type (``str``):
                    N/A
                
        file_type (:obj:`storage.FileType<typegram.api.ayiin.storage.FileType>`):
                    N/A
                
        mtime (``int`` ``32-bit``):
                    N/A
                
        bytes (``bytes``):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            upload.File
            upload.WebFile
            upload.CdnFile
    """

    __slots__: List[str] = ["size", "mime_type", "file_type", "mtime", "bytes"]

    ID = 0x21e753bc
    QUALNAME = "functions.typesupload.WebFile"

    def __init__(self, *, size: int, mime_type: str, file_type: "ayiinstorage.FileType", mtime: int, bytes: bytes) -> None:
        
                self.size = size  # int
        
                self.mime_type = mime_type  # string
        
                self.file_type = file_type  # storage.FileType
        
                self.mtime = mtime  # int
        
                self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebFile":
        # No flags
        
        size = Int.read(b)
        
        mime_type = String.read(b)
        
        file_type = Object.read(b)
        
        mtime = Int.read(b)
        
        bytes = Bytes.read(b)
        
        return WebFile(size=size, mime_type=mime_type, file_type=file_type, mtime=mtime, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.size))
        
        b.write(String(self.mime_type))
        
        b.write(self.file_type.write())
        
        b.write(Int(self.mtime))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()