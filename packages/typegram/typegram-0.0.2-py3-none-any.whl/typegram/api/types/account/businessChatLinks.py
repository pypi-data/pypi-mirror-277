
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



class BusinessChatLinks(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.BusinessChatLinks`.

    Details:
        - Layer: ``181``
        - ID: ``EC43A2D1``

links (List of :obj:`BusinessChatLink<typegram.api.ayiin.BusinessChatLink>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    """

    __slots__: List[str] = ["links", "chats", "users"]

    ID = 0xec43a2d1
    QUALNAME = "types.account.businessChatLinks"

    def __init__(self, *, links: List["api.ayiin.BusinessChatLink"], chats: List["api.ayiin.Chat"], users: List["api.ayiin.User"]) -> None:
        
                self.links = links  # BusinessChatLink
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessChatLinks":
        # No flags
        
        links = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return BusinessChatLinks(links=links, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.links))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()