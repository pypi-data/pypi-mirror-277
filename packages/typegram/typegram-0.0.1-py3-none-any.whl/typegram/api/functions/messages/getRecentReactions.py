
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



class GetRecentReactions(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``39461DB2``

limit (``int`` ``32-bit``):
                    N/A
                
        hash (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`messages.Reactions<typegram.api.ayiin.messages.Reactions>`
    """

    __slots__: List[str] = ["limit", "hash"]

    ID = 0x39461db2
    QUALNAME = "functions.functionsmessages.Reactions"

    def __init__(self, *, limit: int, hash: int) -> None:
        
                self.limit = limit  # int
        
                self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentReactions":
        # No flags
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetRecentReactions(limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()