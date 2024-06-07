
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



class ChatlistUpdates(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.chatlists.ChatlistUpdates`.

    Details:
        - Layer: ``181``
        - ID: ``93BD878D``

missing_peers (List of :obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 25 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            chatlists.ExportedChatlistInvite
            chatlists.ExportedInvites
            chatlists.ChatlistInvite
            chatlists.ChatlistUpdates
    """

    __slots__: List[str] = ["missing_peers", "chats", "users"]

    ID = 0x93bd878d
    QUALNAME = "functions.typeschatlists.ChatlistUpdates"

    def __init__(self, *, missing_peers: List["ayiin.Peer"], chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.missing_peers = missing_peers  # Peer
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatlistUpdates":
        # No flags
        
        missing_peers = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return ChatlistUpdates(missing_peers=missing_peers, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.missing_peers))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()