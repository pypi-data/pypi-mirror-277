
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



class DifferenceEmpty(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.updates.Difference`.

    Details:
        - Layer: ``181``
        - ID: ``5D75A138``

date (``int`` ``32-bit``):
                    N/A
                
        seq (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            updates.Difference
            updates.ChannelDifference
    """

    __slots__: List[str] = ["date", "seq"]

    ID = 0x5d75a138
    QUALNAME = "functions.typesupdates.Difference"

    def __init__(self, *, date: int, seq: int) -> None:
        
                self.date = date  # int
        
                self.seq = seq  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DifferenceEmpty":
        # No flags
        
        date = Int.read(b)
        
        seq = Int.read(b)
        
        return DifferenceEmpty(date=date, seq=seq)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.date))
        
        b.write(Int(self.seq))
        
        return b.getvalue()