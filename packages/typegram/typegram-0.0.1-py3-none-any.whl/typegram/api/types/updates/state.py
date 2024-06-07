
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



class State(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.updates.State`.

    Details:
        - Layer: ``181``
        - ID: ``A56C2A3E``

pts (``int`` ``32-bit``):
                    N/A
                
        qts (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        seq (``int`` ``32-bit``):
                    N/A
                
        unread_count (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 13 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            updates.Difference
            updates.ChannelDifference
    """

    __slots__: List[str] = ["pts", "qts", "date", "seq", "unread_count"]

    ID = 0xa56c2a3e
    QUALNAME = "functions.typesupdates.State"

    def __init__(self, *, pts: int, qts: int, date: int, seq: int, unread_count: int) -> None:
        
                self.pts = pts  # int
        
                self.qts = qts  # int
        
                self.date = date  # int
        
                self.seq = seq  # int
        
                self.unread_count = unread_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "State":
        # No flags
        
        pts = Int.read(b)
        
        qts = Int.read(b)
        
        date = Int.read(b)
        
        seq = Int.read(b)
        
        unread_count = Int.read(b)
        
        return State(pts=pts, qts=qts, date=date, seq=seq, unread_count=unread_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.pts))
        
        b.write(Int(self.qts))
        
        b.write(Int(self.date))
        
        b.write(Int(self.seq))
        
        b.write(Int(self.unread_count))
        
        return b.getvalue()