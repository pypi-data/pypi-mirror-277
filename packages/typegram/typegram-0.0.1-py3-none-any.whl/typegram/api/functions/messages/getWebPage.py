
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



class GetWebPage(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8D9692A3``

url (``str``):
                    N/A
                
        hash (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.WebPage<typegram.api.ayiin.messages.WebPage>`
    """

    __slots__: List[str] = ["url", "hash"]

    ID = 0x8d9692a3
    QUALNAME = "functions.functionsmessages.WebPage"

    def __init__(self, *, url: str, hash: int) -> None:
        
                self.url = url  # string
        
                self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWebPage":
        # No flags
        
        url = String.read(b)
        
        hash = Int.read(b)
        
        return GetWebPage(url=url, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Int(self.hash))
        
        return b.getvalue()