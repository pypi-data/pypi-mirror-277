
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



class SearchSentMedia(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``107E31A0``

q (``str``):
                    N/A
                
        filter (:obj:`MessagesFilter<typegram.api.ayiin.MessagesFilter>`):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.Messages<typegram.api.ayiin.messages.Messages>`
    """

    __slots__: List[str] = ["q", "filter", "limit"]

    ID = 0x107e31a0
    QUALNAME = "functions.functionsmessages.Messages"

    def __init__(self, *, q: str, filter: "ayiin.MessagesFilter", limit: int) -> None:
        
                self.q = q  # string
        
                self.filter = filter  # MessagesFilter
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchSentMedia":
        # No flags
        
        q = String.read(b)
        
        filter = Object.read(b)
        
        limit = Int.read(b)
        
        return SearchSentMedia(q=q, filter=filter, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.q))
        
        b.write(self.filter.write())
        
        b.write(Int(self.limit))
        
        return b.getvalue()