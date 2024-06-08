
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



class MessageActionSecureValuesSent(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``D95C6154``

types (List of :obj:`SecureValueType<typegram.api.ayiin.SecureValueType>`):
                    N/A
                
    """

    __slots__: List[str] = ["types"]

    ID = 0xd95c6154
    QUALNAME = "types.messageActionSecureValuesSent"

    def __init__(self, *, types: List["api.ayiin.SecureValueType"]) -> None:
        
                self.types = types  # SecureValueType

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSecureValuesSent":
        # No flags
        
        types = Object.read(b)
        
        return MessageActionSecureValuesSent(types=types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.types))
        
        return b.getvalue()