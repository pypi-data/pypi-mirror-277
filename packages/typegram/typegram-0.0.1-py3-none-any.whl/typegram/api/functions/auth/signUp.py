
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



class SignUp(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``AAC7B717``

phone_number (``str``):
                    N/A
                
        phone_code_hash (``str``):
                    N/A
                
        first_name (``str``):
                    N/A
                
        last_name (``str``):
                    N/A
                
        no_joined_notifications (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`auth.Authorization<typegram.api.ayiin.auth.Authorization>`
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "first_name", "last_name", "no_joined_notifications"]

    ID = 0xaac7b717
    QUALNAME = "functions.functionsauth.Authorization"

    def __init__(self, *, phone_number: str, phone_code_hash: str, first_name: str, last_name: str, no_joined_notifications: Optional[bool] = None) -> None:
        
                self.phone_number = phone_number  # string
        
                self.phone_code_hash = phone_code_hash  # string
        
                self.first_name = first_name  # string
        
                self.last_name = last_name  # string
        
                self.no_joined_notifications = no_joined_notifications  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SignUp":
        
        flags = Int.read(b)
        
        no_joined_notifications = True if flags & (1 << 0) else False
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        return SignUp(phone_number=phone_number, phone_code_hash=phone_code_hash, first_name=first_name, last_name=last_name, no_joined_notifications=no_joined_notifications)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        return b.getvalue()