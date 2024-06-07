
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



class EligibleToJoin(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.smsjobs.EligibilityToJoin`.

    Details:
        - Layer: ``181``
        - ID: ``DC8B44CF``

terms_url (``str``):
                    N/A
                
        monthly_sent_sms (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["terms_url", "monthly_sent_sms"]

    ID = 0xdc8b44cf
    QUALNAME = "functions.typessmsjobs.EligibilityToJoin"

    def __init__(self, *, terms_url: str, monthly_sent_sms: int) -> None:
        
                self.terms_url = terms_url  # string
        
                self.monthly_sent_sms = monthly_sent_sms  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EligibleToJoin":
        # No flags
        
        terms_url = String.read(b)
        
        monthly_sent_sms = Int.read(b)
        
        return EligibleToJoin(terms_url=terms_url, monthly_sent_sms=monthly_sent_sms)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.terms_url))
        
        b.write(Int(self.monthly_sent_sms))
        
        return b.getvalue()