
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



class UpdateUserStatus(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``E5BDF8DE``

user_id (``int`` ``64-bit``):
                    N/A
                
        status (:obj:`UserStatus<typegram.api.ayiin.UserStatus>`):
                    N/A
                
    """

    __slots__: List[str] = ["user_id", "status"]

    ID = 0xe5bdf8de
    QUALNAME = "types.updateUserStatus"

    def __init__(self, *, user_id: int, status: "api.ayiin.UserStatus") -> None:
        
                self.user_id = user_id  # long
        
                self.status = status  # UserStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserStatus":
        # No flags
        
        user_id = Long.read(b)
        
        status = Object.read(b)
        
        return UpdateUserStatus(user_id=user_id, status=status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(self.status.write())
        
        return b.getvalue()