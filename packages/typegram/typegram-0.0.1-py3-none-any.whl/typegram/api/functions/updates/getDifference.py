
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



class GetDifference(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``19C2F763``

pts (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        qts (``int`` ``32-bit``):
                    N/A
                
        pts_limit (``int`` ``32-bit``, *optional*):
                    N/A
                
        pts_total_limit (``int`` ``32-bit``, *optional*):
                    N/A
                
        qts_limit (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`updates.Difference<typegram.api.ayiin.updates.Difference>`
    """

    __slots__: List[str] = ["pts", "date", "qts", "pts_limit", "pts_total_limit", "qts_limit"]

    ID = 0x19c2f763
    QUALNAME = "functions.functionsupdates.Difference"

    def __init__(self, *, pts: int, date: int, qts: int, pts_limit: Optional[int] = None, pts_total_limit: Optional[int] = None, qts_limit: Optional[int] = None) -> None:
        
                self.pts = pts  # int
        
                self.date = date  # int
        
                self.qts = qts  # int
        
                self.pts_limit = pts_limit  # int
        
                self.pts_total_limit = pts_total_limit  # int
        
                self.qts_limit = qts_limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDifference":
        
        flags = Int.read(b)
        
        pts = Int.read(b)
        
        pts_limit = Int.read(b) if flags & (1 << 1) else None
        pts_total_limit = Int.read(b) if flags & (1 << 0) else None
        date = Int.read(b)
        
        qts = Int.read(b)
        
        qts_limit = Int.read(b) if flags & (1 << 2) else None
        return GetDifference(pts=pts, date=date, qts=qts, pts_limit=pts_limit, pts_total_limit=pts_total_limit, qts_limit=qts_limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.pts))
        
        if self.pts_limit is not None:
            b.write(Int(self.pts_limit))
        
        if self.pts_total_limit is not None:
            b.write(Int(self.pts_total_limit))
        
        b.write(Int(self.date))
        
        b.write(Int(self.qts))
        
        if self.qts_limit is not None:
            b.write(Int(self.qts_limit))
        
        return b.getvalue()