
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



class DifferenceTooLong(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.updates.Difference`.

    Details:
        - Layer: ``181``
        - ID: ``4AFE8F6D``

pts (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            updates.Difference
            updates.ChannelDifference
    """

    __slots__: List[str] = ["pts"]

    ID = 0x4afe8f6d
    QUALNAME = "functions.typesupdates.Difference"

    def __init__(self, *, pts: int) -> None:
        
                self.pts = pts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DifferenceTooLong":
        # No flags
        
        pts = Int.read(b)
        
        return DifferenceTooLong(pts=pts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.pts))
        
        return b.getvalue()