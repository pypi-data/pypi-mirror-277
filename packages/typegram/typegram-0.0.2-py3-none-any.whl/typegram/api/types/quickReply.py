
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class QuickReply(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.QuickReply`.

    Details:
        - Layer: ``181``
        - ID: ``697102B``

shortcut_id (``int`` ``32-bit``):
                    N/A
                
        shortcut (``str``):
                    N/A
                
        top_message (``int`` ``32-bit``):
                    N/A
                
        count (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["shortcut_id", "shortcut", "top_message", "count"]

    ID = 0x697102b
    QUALNAME = "types.quickReply"

    def __init__(self, *, shortcut_id: int, shortcut: str, top_message: int, count: int) -> None:
        
                self.shortcut_id = shortcut_id  # int
        
                self.shortcut = shortcut  # string
        
                self.top_message = top_message  # int
        
                self.count = count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "QuickReply":
        # No flags
        
        shortcut_id = Int.read(b)
        
        shortcut = String.read(b)
        
        top_message = Int.read(b)
        
        count = Int.read(b)
        
        return QuickReply(shortcut_id=shortcut_id, shortcut=shortcut, top_message=top_message, count=count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.shortcut_id))
        
        b.write(String(self.shortcut))
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.count))
        
        return b.getvalue()