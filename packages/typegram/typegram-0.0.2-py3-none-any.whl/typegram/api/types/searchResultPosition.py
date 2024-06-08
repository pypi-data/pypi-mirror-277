
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



class SearchResultPosition(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SearchResultsPosition`.

    Details:
        - Layer: ``181``
        - ID: ``7F648B67``

msg_id (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        offset (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["msg_id", "date", "offset"]

    ID = 0x7f648b67
    QUALNAME = "types.searchResultPosition"

    def __init__(self, *, msg_id: int, date: int, offset: int) -> None:
        
                self.msg_id = msg_id  # int
        
                self.date = date  # int
        
                self.offset = offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchResultPosition":
        # No flags
        
        msg_id = Int.read(b)
        
        date = Int.read(b)
        
        offset = Int.read(b)
        
        return SearchResultPosition(msg_id=msg_id, date=date, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.date))
        
        b.write(Int(self.offset))
        
        return b.getvalue()