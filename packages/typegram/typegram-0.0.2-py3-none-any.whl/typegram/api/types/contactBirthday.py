
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



class ContactBirthday(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ContactBirthday`.

    Details:
        - Layer: ``181``
        - ID: ``1D998733``

contact_id (``int`` ``64-bit``):
                    N/A
                
        birthday (:obj:`Birthday<typegram.api.ayiin.Birthday>`):
                    N/A
                
    """

    __slots__: List[str] = ["contact_id", "birthday"]

    ID = 0x1d998733
    QUALNAME = "types.contactBirthday"

    def __init__(self, *, contact_id: int, birthday: "api.ayiin.Birthday") -> None:
        
                self.contact_id = contact_id  # long
        
                self.birthday = birthday  # Birthday

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ContactBirthday":
        # No flags
        
        contact_id = Long.read(b)
        
        birthday = Object.read(b)
        
        return ContactBirthday(contact_id=contact_id, birthday=birthday)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.contact_id))
        
        b.write(self.birthday.write())
        
        return b.getvalue()