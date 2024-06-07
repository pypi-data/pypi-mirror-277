
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



class ResolvePhone(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8AF94344``

phone (``str``):
                    N/A
                
    Returns:
        :obj:`contacts.ResolvedPeer<typegram.api.ayiin.contacts.ResolvedPeer>`
    """

    __slots__: List[str] = ["phone"]

    ID = 0x8af94344
    QUALNAME = "functions.functionscontacts.ResolvedPeer"

    def __init__(self, *, phone: str) -> None:
        
                self.phone = phone  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolvePhone":
        # No flags
        
        phone = String.read(b)
        
        return ResolvePhone(phone=phone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.phone))
        
        return b.getvalue()