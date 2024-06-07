
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



class InvokeWithMessagesRange(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``365275F2``

range (:obj:`MessageRange<typegram.api.ayiin.MessageRange>`):
                    N/A
                
        query (``!x``):
                    N/A
                
    Returns:
        Any object from :obj:`~typegram.api.types`
    """

    __slots__: List[str] = ["range", "query"]

    ID = 0x365275f2
    QUALNAME = "functions.functions.X"

    def __init__(self, *, range: "ayiin.MessageRange", query: bytes) -> None:
        
                self.range = range  # MessageRange
        
                self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithMessagesRange":
        # No flags
        
        range = Object.read(b)
        
        query = !X.read(b)
        
        return InvokeWithMessagesRange(range=range, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.range.write())
        
        b.write(!X(self.query))
        
        return b.getvalue()