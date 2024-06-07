
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



class Contacts(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.contacts.Contacts`.

    Details:
        - Layer: ``181``
        - ID: ``EAE87E42``

contacts (List of :obj:`Contact<typegram.api.ayiin.Contact>`):
                    N/A
                
        saved_count (``int`` ``32-bit``):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

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

    __slots__: List[str] = ["contacts", "saved_count", "users"]

    ID = 0xeae87e42
    QUALNAME = "functions.typescontacts.Contacts"

    def __init__(self, *, contacts: List["ayiin.Contact"], saved_count: int, users: List["ayiin.User"]) -> None:
        
                self.contacts = contacts  # Contact
        
                self.saved_count = saved_count  # int
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Contacts":
        # No flags
        
        contacts = Object.read(b)
        
        saved_count = Int.read(b)
        
        users = Object.read(b)
        
        return Contacts(contacts=contacts, saved_count=saved_count, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.contacts))
        
        b.write(Int(self.saved_count))
        
        b.write(Vector(self.users))
        
        return b.getvalue()