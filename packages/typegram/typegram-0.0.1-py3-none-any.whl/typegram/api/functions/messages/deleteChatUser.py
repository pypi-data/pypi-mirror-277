
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



class DeleteChatUser(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A2185CAB``

chat_id (``int`` ``64-bit``):
                    N/A
                
        user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        revoke_history (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["chat_id", "user_id", "revoke_history"]

    ID = 0xa2185cab
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, chat_id: int, user_id: "ayiin.InputUser", revoke_history: Optional[bool] = None) -> None:
        
                self.chat_id = chat_id  # long
        
                self.user_id = user_id  # InputUser
        
                self.revoke_history = revoke_history  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteChatUser":
        
        flags = Int.read(b)
        
        revoke_history = True if flags & (1 << 0) else False
        chat_id = Long.read(b)
        
        user_id = Object.read(b)
        
        return DeleteChatUser(chat_id=chat_id, user_id=user_id, revoke_history=revoke_history)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.chat_id))
        
        b.write(self.user_id.write())
        
        return b.getvalue()