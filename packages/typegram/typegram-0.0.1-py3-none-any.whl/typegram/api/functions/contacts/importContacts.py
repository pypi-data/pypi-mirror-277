
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



class ImportContacts(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``2C800BE5``

contacts (List of :obj:`InputContact<typegram.api.ayiin.InputContact>`):
                    N/A
                
    Returns:
        :obj:`contacts.ImportedContacts<typegram.api.ayiin.contacts.ImportedContacts>`
    """

    __slots__: List[str] = ["contacts"]

    ID = 0x2c800be5
    QUALNAME = "functions.functionscontacts.ImportedContacts"

    def __init__(self, *, contacts: List["ayiin.InputContact"]) -> None:
        
                self.contacts = contacts  # InputContact

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportContacts":
        # No flags
        
        contacts = Object.read(b)
        
        return ImportContacts(contacts=contacts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.contacts))
        
        return b.getvalue()