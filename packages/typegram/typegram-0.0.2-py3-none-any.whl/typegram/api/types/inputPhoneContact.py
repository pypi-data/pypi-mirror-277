
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



class InputPhoneContact(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputContact`.

    Details:
        - Layer: ``181``
        - ID: ``F392B7F4``

client_id (``int`` ``64-bit``):
                    N/A
                
        phone (``str``):
                    N/A
                
        first_name (``str``):
                    N/A
                
        last_name (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["client_id", "phone", "first_name", "last_name"]

    ID = 0xf392b7f4
    QUALNAME = "types.inputPhoneContact"

    def __init__(self, *, client_id: int, phone: str, first_name: str, last_name: str) -> None:
        
                self.client_id = client_id  # long
        
                self.phone = phone  # string
        
                self.first_name = first_name  # string
        
                self.last_name = last_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPhoneContact":
        # No flags
        
        client_id = Long.read(b)
        
        phone = String.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        return InputPhoneContact(client_id=client_id, phone=phone, first_name=first_name, last_name=last_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.client_id))
        
        b.write(String(self.phone))
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        return b.getvalue()