
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



class InvokeWithTakeout(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``ACA9FD2E``

takeout_id (``int`` ``64-bit``):
                    N/A
                
        query (``!x``):
                    N/A
                
    Returns:
        Any object from :obj:`~typegram.api.types`
    """

    __slots__: List[str] = ["takeout_id", "query"]

    ID = 0xaca9fd2e
    QUALNAME = "functions.functions.X"

    def __init__(self, *, takeout_id: int, query: bytes) -> None:
        
                self.takeout_id = takeout_id  # long
        
                self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithTakeout":
        # No flags
        
        takeout_id = Long.read(b)
        
        query = !X.read(b)
        
        return InvokeWithTakeout(takeout_id=takeout_id, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.takeout_id))
        
        b.write(!X(self.query))
        
        return b.getvalue()