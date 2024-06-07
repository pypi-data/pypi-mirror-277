
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



class FileCdnRedirect(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.upload.File`.

    Details:
        - Layer: ``181``
        - ID: ``F18CDA44``

dc_id (``int`` ``32-bit``):
                    N/A
                
        file_token (``bytes``):
                    N/A
                
        encryption_key (``bytes``):
                    N/A
                
        encryption_iv (``bytes``):
                    N/A
                
        file_hashes (List of :obj:`FileHash<typegram.api.ayiin.FileHash>`):
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

    __slots__: List[str] = ["dc_id", "file_token", "encryption_key", "encryption_iv", "file_hashes"]

    ID = 0xf18cda44
    QUALNAME = "functions.typesupload.File"

    def __init__(self, *, dc_id: int, file_token: bytes, encryption_key: bytes, encryption_iv: bytes, file_hashes: List["ayiin.FileHash"]) -> None:
        
                self.dc_id = dc_id  # int
        
                self.file_token = file_token  # bytes
        
                self.encryption_key = encryption_key  # bytes
        
                self.encryption_iv = encryption_iv  # bytes
        
                self.file_hashes = file_hashes  # FileHash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FileCdnRedirect":
        # No flags
        
        dc_id = Int.read(b)
        
        file_token = Bytes.read(b)
        
        encryption_key = Bytes.read(b)
        
        encryption_iv = Bytes.read(b)
        
        file_hashes = Object.read(b)
        
        return FileCdnRedirect(dc_id=dc_id, file_token=file_token, encryption_key=encryption_key, encryption_iv=encryption_iv, file_hashes=file_hashes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.dc_id))
        
        b.write(Bytes(self.file_token))
        
        b.write(Bytes(self.encryption_key))
        
        b.write(Bytes(self.encryption_iv))
        
        b.write(Vector(self.file_hashes))
        
        return b.getvalue()