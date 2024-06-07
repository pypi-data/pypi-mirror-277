
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



class RequestEncryption(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F64DAF43``

user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        random_id (``int`` ``32-bit``):
                    N/A
                
        g_a (``bytes``):
                    N/A
                
    Returns:
        :obj:`EncryptedChat<typegram.api.ayiin.EncryptedChat>`
    """

    __slots__: List[str] = ["user_id", "random_id", "g_a"]

    ID = 0xf64daf43
    QUALNAME = "functions.functions.EncryptedChat"

    def __init__(self, *, user_id: "ayiin.InputUser", random_id: int, g_a: bytes) -> None:
        
                self.user_id = user_id  # InputUser
        
                self.random_id = random_id  # int
        
                self.g_a = g_a  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestEncryption":
        # No flags
        
        user_id = Object.read(b)
        
        random_id = Int.read(b)
        
        g_a = Bytes.read(b)
        
        return RequestEncryption(user_id=user_id, random_id=random_id, g_a=g_a)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(Int(self.random_id))
        
        b.write(Bytes(self.g_a))
        
        return b.getvalue()