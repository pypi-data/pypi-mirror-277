
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



class UserStatusLastMonth(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.UserStatus`.

    Details:
        - Layer: ``181``
        - ID: ``65899777``

by_me (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["by_me"]

    ID = 0x65899777
    QUALNAME = "types.userStatusLastMonth"

    def __init__(self, *, by_me: Optional[bool] = None) -> None:
        
                self.by_me = by_me  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserStatusLastMonth":
        
        flags = Int.read(b)
        
        by_me = True if flags & (1 << 0) else False
        return UserStatusLastMonth(by_me=by_me)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()