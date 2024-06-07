
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



class AddContact(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E8F463D0``

id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        first_name (``str``):
                    N/A
                
        last_name (``str``):
                    N/A
                
        phone (``str``):
                    N/A
                
        add_phone_privacy_exception (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["id", "first_name", "last_name", "phone", "add_phone_privacy_exception"]

    ID = 0xe8f463d0
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, id: "ayiin.InputUser", first_name: str, last_name: str, phone: str, add_phone_privacy_exception: Optional[bool] = None) -> None:
        
                self.id = id  # InputUser
        
                self.first_name = first_name  # string
        
                self.last_name = last_name  # string
        
                self.phone = phone  # string
        
                self.add_phone_privacy_exception = add_phone_privacy_exception  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AddContact":
        
        flags = Int.read(b)
        
        add_phone_privacy_exception = True if flags & (1 << 0) else False
        id = Object.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        phone = String.read(b)
        
        return AddContact(id=id, first_name=first_name, last_name=last_name, phone=phone, add_phone_privacy_exception=add_phone_privacy_exception)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        b.write(String(self.phone))
        
        return b.getvalue()