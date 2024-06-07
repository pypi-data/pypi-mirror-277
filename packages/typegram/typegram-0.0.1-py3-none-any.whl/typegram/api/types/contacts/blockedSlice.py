
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



class BlockedSlice(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.contacts.Blocked`.

    Details:
        - Layer: ``181``
        - ID: ``E1664194``

count (``int`` ``32-bit``):
                    N/A
                
        blocked (List of :obj:`PeerBlocked<typegram.api.ayiin.PeerBlocked>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            contacts.Contacts
            contacts.ImportedContacts
            contacts.Blocked
            contacts.Found
            contacts.ResolvedPeer
            contacts.TopPeers
    """

    __slots__: List[str] = ["count", "blocked", "chats", "users"]

    ID = 0xe1664194
    QUALNAME = "functions.typescontacts.Blocked"

    def __init__(self, *, count: int, blocked: List["ayiin.PeerBlocked"], chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.count = count  # int
        
                self.blocked = blocked  # PeerBlocked
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BlockedSlice":
        # No flags
        
        count = Int.read(b)
        
        blocked = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return BlockedSlice(count=count, blocked=blocked, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.blocked))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()