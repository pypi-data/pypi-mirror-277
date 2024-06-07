
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



class GetUsers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D91A548``

id (List of :obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
    Returns:
        List of :obj:`User<typegram.api.ayiin.User>`
    """

    __slots__: List[str] = ["id"]

    ID = 0xd91a548
    QUALNAME = "functions.functions.Vector<User>"

    def __init__(self, *, id: List["ayiin.InputUser"]) -> None:
        
                self.id = id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUsers":
        # No flags
        
        id = Object.read(b)
        
        return GetUsers(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id))
        
        return b.getvalue()