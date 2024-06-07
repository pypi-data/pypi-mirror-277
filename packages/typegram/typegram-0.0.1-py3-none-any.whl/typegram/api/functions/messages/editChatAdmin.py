
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



class EditChatAdmin(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A85BD1C2``

chat_id (``int`` ``64-bit``):
                    N/A
                
        user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        is_admin (``bool``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["chat_id", "user_id", "is_admin"]

    ID = 0xa85bd1c2
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, chat_id: int, user_id: "ayiin.InputUser", is_admin: bool) -> None:
        
                self.chat_id = chat_id  # long
        
                self.user_id = user_id  # InputUser
        
                self.is_admin = is_admin  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatAdmin":
        # No flags
        
        chat_id = Long.read(b)
        
        user_id = Object.read(b)
        
        is_admin = Bool.read(b)
        
        return EditChatAdmin(chat_id=chat_id, user_id=user_id, is_admin=is_admin)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        b.write(self.user_id.write())
        
        b.write(Bool(self.is_admin))
        
        return b.getvalue()