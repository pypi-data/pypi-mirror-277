
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



class InputPrivacyValueAllowUsers(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputPrivacyRule`.

    Details:
        - Layer: ``181``
        - ID: ``131CC67F``

users (List of :obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
    """

    __slots__: List[str] = ["users"]

    ID = 0x131cc67f
    QUALNAME = "types.inputPrivacyValueAllowUsers"

    def __init__(self, *, users: List["api.ayiin.InputUser"]) -> None:
        
                self.users = users  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPrivacyValueAllowUsers":
        # No flags
        
        users = Object.read(b)
        
        return InputPrivacyValueAllowUsers(users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.users))
        
        return b.getvalue()