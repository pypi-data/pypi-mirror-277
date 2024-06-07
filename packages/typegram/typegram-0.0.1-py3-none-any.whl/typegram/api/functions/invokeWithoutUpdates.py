
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



class InvokeWithoutUpdates(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``BF9459B7``

query (``!x``):
                    N/A
                
    Returns:
        Any object from :obj:`~typegram.api.types`
    """

    __slots__: List[str] = ["query"]

    ID = 0xbf9459b7
    QUALNAME = "functions.functions.X"

    def __init__(self, *, query: bytes) -> None:
        
                self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithoutUpdates":
        # No flags
        
        query = !X.read(b)
        
        return InvokeWithoutUpdates(query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(!X(self.query))
        
        return b.getvalue()