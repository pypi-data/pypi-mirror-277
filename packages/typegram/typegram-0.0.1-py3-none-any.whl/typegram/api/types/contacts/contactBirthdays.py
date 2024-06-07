
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



class ContactBirthdays(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.contacts.ContactBirthdays`.

    Details:
        - Layer: ``181``
        - ID: ``114FF30D``

contacts (List of :obj:`ContactBirthday<typegram.api.ayiin.ContactBirthday>`):
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

    __slots__: List[str] = ["contacts", "users"]

    ID = 0x114ff30d
    QUALNAME = "functions.typescontacts.ContactBirthdays"

    def __init__(self, *, contacts: List["ayiin.ContactBirthday"], users: List["ayiin.User"]) -> None:
        
                self.contacts = contacts  # ContactBirthday
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ContactBirthdays":
        # No flags
        
        contacts = Object.read(b)
        
        users = Object.read(b)
        
        return ContactBirthdays(contacts=contacts, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.contacts))
        
        b.write(Vector(self.users))
        
        return b.getvalue()