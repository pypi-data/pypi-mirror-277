
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



class ReportMissingCode(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``CB9DEFF6``

phone_number (``str``):
                    N/A
                
        phone_code_hash (``str``):
                    N/A
                
        mnc (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "mnc"]

    ID = 0xcb9deff6
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, phone_number: str, phone_code_hash: str, mnc: str) -> None:
        
                self.phone_number = phone_number  # string
        
                self.phone_code_hash = phone_code_hash  # string
        
                self.mnc = mnc  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportMissingCode":
        # No flags
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        mnc = String.read(b)
        
        return ReportMissingCode(phone_number=phone_number, phone_code_hash=phone_code_hash, mnc=mnc)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        b.write(String(self.mnc))
        
        return b.getvalue()