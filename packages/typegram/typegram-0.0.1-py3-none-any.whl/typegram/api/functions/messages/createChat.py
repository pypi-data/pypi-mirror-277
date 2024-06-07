
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



class CreateChat(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``92CEDDD4``

users (List of :obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        title (``str``):
                    N/A
                
        ttl_period (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.InvitedUsers<typegram.api.ayiin.messages.InvitedUsers>`
    """

    __slots__: List[str] = ["users", "title", "ttl_period"]

    ID = 0x92ceddd4
    QUALNAME = "functions.functionsmessages.InvitedUsers"

    def __init__(self, *, users: List["ayiin.InputUser"], title: str, ttl_period: Optional[int] = None) -> None:
        
                self.users = users  # InputUser
        
                self.title = title  # string
        
                self.ttl_period = ttl_period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateChat":
        
        flags = Int.read(b)
        
        users = Object.read(b)
        
        title = String.read(b)
        
        ttl_period = Int.read(b) if flags & (1 << 0) else None
        return CreateChat(users=users, title=title, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.users))
        
        b.write(String(self.title))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()