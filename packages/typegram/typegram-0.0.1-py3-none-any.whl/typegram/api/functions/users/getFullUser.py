
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



class GetFullUser(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B60F5918``

id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
    Returns:
        :obj:`users.UserFull<typegram.api.ayiin.users.UserFull>`
    """

    __slots__: List[str] = ["id"]

    ID = 0xb60f5918
    QUALNAME = "functions.functionsusers.UserFull"

    def __init__(self, *, id: "ayiin.InputUser") -> None:
        
                self.id = id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFullUser":
        # No flags
        
        id = Object.read(b)
        
        return GetFullUser(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        return b.getvalue()