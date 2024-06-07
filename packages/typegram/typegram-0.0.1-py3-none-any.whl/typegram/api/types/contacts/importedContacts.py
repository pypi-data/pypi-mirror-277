
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



class ImportedContacts(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.contacts.ImportedContacts`.

    Details:
        - Layer: ``181``
        - ID: ``77D01C3B``

imported (List of :obj:`ImportedContact<typegram.api.ayiin.ImportedContact>`):
                    N/A
                
        popular_invites (List of :obj:`PopularContact<typegram.api.ayiin.PopularContact>`):
                    N/A
                
        retry_contacts (List of ``int`` ``64-bit``):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 25 functions.

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

    __slots__: List[str] = ["imported", "popular_invites", "retry_contacts", "users"]

    ID = 0x77d01c3b
    QUALNAME = "functions.typescontacts.ImportedContacts"

    def __init__(self, *, imported: List["ayiin.ImportedContact"], popular_invites: List["ayiin.PopularContact"], retry_contacts: List[int], users: List["ayiin.User"]) -> None:
        
                self.imported = imported  # ImportedContact
        
                self.popular_invites = popular_invites  # PopularContact
        
                self.retry_contacts = retry_contacts  # long
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportedContacts":
        # No flags
        
        imported = Object.read(b)
        
        popular_invites = Object.read(b)
        
        retry_contacts = Object.read(b, Long)
        
        users = Object.read(b)
        
        return ImportedContacts(imported=imported, popular_invites=popular_invites, retry_contacts=retry_contacts, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.imported))
        
        b.write(Vector(self.popular_invites))
        
        b.write(Vector(self.retry_contacts, Long))
        
        b.write(Vector(self.users))
        
        return b.getvalue()