
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



class Search(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``11F812D8``

q (``str``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`contacts.Found<typegram.api.ayiin.contacts.Found>`
    """

    __slots__: List[str] = ["q", "limit"]

    ID = 0x11f812d8
    QUALNAME = "functions.functionscontacts.Found"

    def __init__(self, *, q: str, limit: int) -> None:
        
                self.q = q  # string
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Search":
        # No flags
        
        q = String.read(b)
        
        limit = Int.read(b)
        
        return Search(q=q, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.q))
        
        b.write(Int(self.limit))
        
        return b.getvalue()