
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



class GetMyStickers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D0B5E1FC``

offset_id (``int`` ``64-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.MyStickers<typegram.api.ayiin.messages.MyStickers>`
    """

    __slots__: List[str] = ["offset_id", "limit"]

    ID = 0xd0b5e1fc
    QUALNAME = "functions.functionsmessages.MyStickers"

    def __init__(self, *, offset_id: int, limit: int) -> None:
        
                self.offset_id = offset_id  # long
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMyStickers":
        # No flags
        
        offset_id = Long.read(b)
        
        limit = Int.read(b)
        
        return GetMyStickers(offset_id=offset_id, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()