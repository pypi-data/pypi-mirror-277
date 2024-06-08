
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



class UpdateReadMessagesContents(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``F8227181``

messages (List of ``int`` ``32-bit``):
                    N/A
                
        pts (``int`` ``32-bit``):
                    N/A
                
        pts_count (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["messages", "pts", "pts_count", "date"]

    ID = 0xf8227181
    QUALNAME = "types.updateReadMessagesContents"

    def __init__(self, *, messages: List[int], pts: int, pts_count: int, date: Optional[int] = None) -> None:
        
                self.messages = messages  # int
        
                self.pts = pts  # int
        
                self.pts_count = pts_count  # int
        
                self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadMessagesContents":
        
        flags = Int.read(b)
        
        messages = Object.read(b, Int)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        date = Int.read(b) if flags & (1 << 0) else None
        return UpdateReadMessagesContents(messages=messages, pts=pts, pts_count=pts_count, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.messages, Int))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        if self.date is not None:
            b.write(Int(self.date))
        
        return b.getvalue()