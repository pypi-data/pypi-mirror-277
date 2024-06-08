
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



class SecureValueErrorData(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SecureValueError`.

    Details:
        - Layer: ``181``
        - ID: ``E8A40BD9``

type (:obj:`SecureValueType<typegram.api.ayiin.SecureValueType>`):
                    N/A
                
        data_hash (``bytes``):
                    N/A
                
        field (``str``):
                    N/A
                
        text (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["type", "data_hash", "field", "text"]

    ID = 0xe8a40bd9
    QUALNAME = "types.secureValueErrorData"

    def __init__(self, *, type: "api.ayiin.SecureValueType", data_hash: bytes, field: str, text: str) -> None:
        
                self.type = type  # SecureValueType
        
                self.data_hash = data_hash  # bytes
        
                self.field = field  # string
        
                self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueErrorData":
        # No flags
        
        type = Object.read(b)
        
        data_hash = Bytes.read(b)
        
        field = String.read(b)
        
        text = String.read(b)
        
        return SecureValueErrorData(type=type, data_hash=data_hash, field=field, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.type.write())
        
        b.write(Bytes(self.data_hash))
        
        b.write(String(self.field))
        
        b.write(String(self.text))
        
        return b.getvalue()