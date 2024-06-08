
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



class SecureValue(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SecureValue`.

    Details:
        - Layer: ``181``
        - ID: ``187FA0CA``

type (:obj:`SecureValueType<typegram.api.ayiin.SecureValueType>`):
                    N/A
                
        hash (``bytes``):
                    N/A
                
        data (:obj:`SecureData<typegram.api.ayiin.SecureData>`, *optional*):
                    N/A
                
        front_side (:obj:`SecureFile<typegram.api.ayiin.SecureFile>`, *optional*):
                    N/A
                
        reverse_side (:obj:`SecureFile<typegram.api.ayiin.SecureFile>`, *optional*):
                    N/A
                
        is_selfie (:obj:`SecureFile<typegram.api.ayiin.SecureFile>`, *optional*):
                    N/A
                
        translation (List of :obj:`SecureFile<typegram.api.ayiin.SecureFile>`, *optional*):
                    N/A
                
        files (List of :obj:`SecureFile<typegram.api.ayiin.SecureFile>`, *optional*):
                    N/A
                
        plain_data (:obj:`SecurePlainData<typegram.api.ayiin.SecurePlainData>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 11 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            account.getSecureValue
            account.saveSecureValue
    """

    __slots__: List[str] = ["type", "hash", "data", "front_side", "reverse_side", "is_selfie", "translation", "files", "plain_data"]

    ID = 0x187fa0ca
    QUALNAME = "types.secureValue"

    def __init__(self, *, type: "api.ayiin.SecureValueType", hash: bytes, data: "api.ayiin.SecureData" = None, front_side: "api.ayiin.SecureFile" = None, reverse_side: "api.ayiin.SecureFile" = None, is_selfie: "api.ayiin.SecureFile" = None, translation: Optional[List["api.ayiin.SecureFile"]] = None, files: Optional[List["api.ayiin.SecureFile"]] = None, plain_data: "api.ayiin.SecurePlainData" = None) -> None:
        
                self.type = type  # SecureValueType
        
                self.hash = hash  # bytes
        
                self.data = data  # SecureData
        
                self.front_side = front_side  # SecureFile
        
                self.reverse_side = reverse_side  # SecureFile
        
                self.is_selfie = is_selfie  # SecureFile
        
                self.translation = translation  # SecureFile
        
                self.files = files  # SecureFile
        
                self.plain_data = plain_data  # SecurePlainData

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValue":
        
        flags = Int.read(b)
        
        type = Object.read(b)
        
        data = Object.read(b) if flags & (1 << 0) else None
        
        front_side = Object.read(b) if flags & (1 << 1) else None
        
        reverse_side = Object.read(b) if flags & (1 << 2) else None
        
        is_selfie = Object.read(b) if flags & (1 << 3) else None
        
        translation = Object.read(b) if flags & (1 << 6) else []
        
        files = Object.read(b) if flags & (1 << 4) else []
        
        plain_data = Object.read(b) if flags & (1 << 5) else None
        
        hash = Bytes.read(b)
        
        return SecureValue(type=type, hash=hash, data=data, front_side=front_side, reverse_side=reverse_side, is_selfie=is_selfie, translation=translation, files=files, plain_data=plain_data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.type.write())
        
        if self.data is not None:
            b.write(self.data.write())
        
        if self.front_side is not None:
            b.write(self.front_side.write())
        
        if self.reverse_side is not None:
            b.write(self.reverse_side.write())
        
        if self.is_selfie is not None:
            b.write(self.is_selfie.write())
        
        if self.translation is not None:
            b.write(Vector(self.translation))
        
        if self.files is not None:
            b.write(Vector(self.files))
        
        if self.plain_data is not None:
            b.write(self.plain_data.write())
        
        b.write(Bytes(self.hash))
        
        return b.getvalue()