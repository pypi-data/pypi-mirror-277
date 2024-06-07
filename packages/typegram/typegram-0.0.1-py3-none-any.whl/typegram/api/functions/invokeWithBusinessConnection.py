
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



class InvokeWithBusinessConnection(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``DD289F8E``

connection_id (``str``):
                    N/A
                
        query (``!x``):
                    N/A
                
    Returns:
        Any object from :obj:`~typegram.api.types`
    """

    __slots__: List[str] = ["connection_id", "query"]

    ID = 0xdd289f8e
    QUALNAME = "functions.functions.X"

    def __init__(self, *, connection_id: str, query: bytes) -> None:
        
                self.connection_id = connection_id  # string
        
                self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithBusinessConnection":
        # No flags
        
        connection_id = String.read(b)
        
        query = !X.read(b)
        
        return InvokeWithBusinessConnection(connection_id=connection_id, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.connection_id))
        
        b.write(!X(self.query))
        
        return b.getvalue()