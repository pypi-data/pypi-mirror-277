
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



class UpdateBirthday(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``CC6E0C11``

birthday (:obj:`Birthday<typegram.api.ayiin.Birthday>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["birthday"]

    ID = 0xcc6e0c11
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, birthday: "ayiin.Birthday" = None) -> None:
        
                self.birthday = birthday  # Birthday

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBirthday":
        
        flags = Int.read(b)
        
        birthday = Object.read(b) if flags & (1 << 0) else None
        
        return UpdateBirthday(birthday=birthday)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.birthday is not None:
            b.write(self.birthday.write())
        
        return b.getvalue()