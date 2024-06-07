
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



class AddChatUser(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``CBC6D107``

chat_id (``int`` ``64-bit``):
                    N/A
                
        user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        fwd_limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.InvitedUsers<typegram.api.ayiin.messages.InvitedUsers>`
    """

    __slots__: List[str] = ["chat_id", "user_id", "fwd_limit"]

    ID = 0xcbc6d107
    QUALNAME = "functions.functionsmessages.InvitedUsers"

    def __init__(self, *, chat_id: int, user_id: "ayiin.InputUser", fwd_limit: int) -> None:
        
                self.chat_id = chat_id  # long
        
                self.user_id = user_id  # InputUser
        
                self.fwd_limit = fwd_limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AddChatUser":
        # No flags
        
        chat_id = Long.read(b)
        
        user_id = Object.read(b)
        
        fwd_limit = Int.read(b)
        
        return AddChatUser(chat_id=chat_id, user_id=user_id, fwd_limit=fwd_limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        b.write(self.user_id.write())
        
        b.write(Int(self.fwd_limit))
        
        return b.getvalue()