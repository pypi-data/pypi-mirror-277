
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



class Found(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.contacts.Found`.

    Details:
        - Layer: ``181``
        - ID: ``B3134D9D``

my_results (List of :obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        results (List of :obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

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

    __slots__: List[str] = ["my_results", "results", "chats", "users"]

    ID = 0xb3134d9d
    QUALNAME = "functions.typescontacts.Found"

    def __init__(self, *, my_results: List["ayiin.Peer"], results: List["ayiin.Peer"], chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.my_results = my_results  # Peer
        
                self.results = results  # Peer
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Found":
        # No flags
        
        my_results = Object.read(b)
        
        results = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return Found(my_results=my_results, results=results, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.my_results))
        
        b.write(Vector(self.results))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()