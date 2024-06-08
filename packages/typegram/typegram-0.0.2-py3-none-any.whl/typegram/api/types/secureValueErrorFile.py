
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



class SecureValueErrorFile(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SecureValueError`.

    Details:
        - Layer: ``181``
        - ID: ``7A700873``

type (:obj:`SecureValueType<typegram.api.ayiin.SecureValueType>`):
                    N/A
                
        file_hash (``bytes``):
                    N/A
                
        text (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["type", "file_hash", "text"]

    ID = 0x7a700873
    QUALNAME = "types.secureValueErrorFile"

    def __init__(self, *, type: "api.ayiin.SecureValueType", file_hash: bytes, text: str) -> None:
        
                self.type = type  # SecureValueType
        
                self.file_hash = file_hash  # bytes
        
                self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueErrorFile":
        # No flags
        
        type = Object.read(b)
        
        file_hash = Bytes.read(b)
        
        text = String.read(b)
        
        return SecureValueErrorFile(type=type, file_hash=file_hash, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.type.write())
        
        b.write(Bytes(self.file_hash))
        
        b.write(String(self.text))
        
        return b.getvalue()