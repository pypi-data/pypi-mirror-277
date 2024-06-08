
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



class StoryItemSkipped(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StoryItem`.

    Details:
        - Layer: ``181``
        - ID: ``FFADC913``

id (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        expire_date (``int`` ``32-bit``):
                    N/A
                
        close_friends (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "date", "expire_date", "close_friends"]

    ID = 0xffadc913
    QUALNAME = "types.storyItemSkipped"

    def __init__(self, *, id: int, date: int, expire_date: int, close_friends: Optional[bool] = None) -> None:
        
                self.id = id  # int
        
                self.date = date  # int
        
                self.expire_date = expire_date  # int
        
                self.close_friends = close_friends  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryItemSkipped":
        
        flags = Int.read(b)
        
        close_friends = True if flags & (1 << 8) else False
        id = Int.read(b)
        
        date = Int.read(b)
        
        expire_date = Int.read(b)
        
        return StoryItemSkipped(id=id, date=date, expire_date=expire_date, close_friends=close_friends)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Int(self.date))
        
        b.write(Int(self.expire_date))
        
        return b.getvalue()