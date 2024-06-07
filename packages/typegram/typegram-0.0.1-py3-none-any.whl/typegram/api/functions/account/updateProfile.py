
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



class UpdateProfile(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``78515775``

first_name (``str``, *optional*):
                    N/A
                
        last_name (``str``, *optional*):
                    N/A
                
        about (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`User<typegram.api.ayiin.User>`
    """

    __slots__: List[str] = ["first_name", "last_name", "about"]

    ID = 0x78515775
    QUALNAME = "functions.functions.User"

    def __init__(self, *, first_name: Optional[str] = None, last_name: Optional[str] = None, about: Optional[str] = None) -> None:
        
                self.first_name = first_name  # string
        
                self.last_name = last_name  # string
        
                self.about = about  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateProfile":
        
        flags = Int.read(b)
        
        first_name = String.read(b) if flags & (1 << 0) else None
        last_name = String.read(b) if flags & (1 << 1) else None
        about = String.read(b) if flags & (1 << 2) else None
        return UpdateProfile(first_name=first_name, last_name=last_name, about=about)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.first_name is not None:
            b.write(String(self.first_name))
        
        if self.last_name is not None:
            b.write(String(self.last_name))
        
        if self.about is not None:
            b.write(String(self.about))
        
        return b.getvalue()