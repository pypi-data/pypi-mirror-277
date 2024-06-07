
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



class File(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.upload.File`.

    Details:
        - Layer: ``181``
        - ID: ``96A18D5``

type (:obj:`storage.FileType<typegram.api.ayiin.storage.FileType>`):
                    N/A
                
        mtime (``int`` ``32-bit``):
                    N/A
                
        bytes (``bytes``):
                    N/A
                
    Functions:
        This object can be returned by 11 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            upload.File
            upload.WebFile
            upload.CdnFile
    """

    __slots__: List[str] = ["type", "mtime", "bytes"]

    ID = 0x96a18d5
    QUALNAME = "functions.typesupload.File"

    def __init__(self, *, type: "ayiinstorage.FileType", mtime: int, bytes: bytes) -> None:
        
                self.type = type  # storage.FileType
        
                self.mtime = mtime  # int
        
                self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "File":
        # No flags
        
        type = Object.read(b)
        
        mtime = Int.read(b)
        
        bytes = Bytes.read(b)
        
        return File(type=type, mtime=mtime, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.type.write())
        
        b.write(Int(self.mtime))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()