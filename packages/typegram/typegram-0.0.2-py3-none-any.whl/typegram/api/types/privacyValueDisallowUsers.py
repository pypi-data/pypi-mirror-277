
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



class PrivacyValueDisallowUsers(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PrivacyRule`.

    Details:
        - Layer: ``181``
        - ID: ``E4621141``

users (List of ``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["users"]

    ID = 0xe4621141
    QUALNAME = "types.privacyValueDisallowUsers"

    def __init__(self, *, users: List[int]) -> None:
        
                self.users = users  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PrivacyValueDisallowUsers":
        # No flags
        
        users = Object.read(b, Long)
        
        return PrivacyValueDisallowUsers(users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.users, Long))
        
        return b.getvalue()