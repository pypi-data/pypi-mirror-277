
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



class MessageActionChatAddUser(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``15CEFD00``

users (List of ``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["users"]

    ID = 0x15cefd00
    QUALNAME = "types.messageActionChatAddUser"

    def __init__(self, *, users: List[int]) -> None:
        
                self.users = users  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionChatAddUser":
        # No flags
        
        users = Object.read(b, Long)
        
        return MessageActionChatAddUser(users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.users, Long))
        
        return b.getvalue()