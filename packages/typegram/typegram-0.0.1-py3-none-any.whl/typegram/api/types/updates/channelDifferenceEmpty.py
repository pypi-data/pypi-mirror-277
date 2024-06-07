
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



class ChannelDifferenceEmpty(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.updates.ChannelDifference`.

    Details:
        - Layer: ``181``
        - ID: ``3E11AFFB``

pts (``int`` ``32-bit``):
                    N/A
                
        final (``bool``, *optional*):
                    N/A
                
        timeout (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 25 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            updates.Difference
            updates.ChannelDifference
    """

    __slots__: List[str] = ["pts", "final", "timeout"]

    ID = 0x3e11affb
    QUALNAME = "functions.typesupdates.ChannelDifference"

    def __init__(self, *, pts: int, final: Optional[bool] = None, timeout: Optional[int] = None) -> None:
        
                self.pts = pts  # int
        
                self.final = final  # true
        
                self.timeout = timeout  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelDifferenceEmpty":
        
        flags = Int.read(b)
        
        final = True if flags & (1 << 0) else False
        pts = Int.read(b)
        
        timeout = Int.read(b) if flags & (1 << 1) else None
        return ChannelDifferenceEmpty(pts=pts, final=final, timeout=timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.pts))
        
        if self.timeout is not None:
            b.write(Int(self.timeout))
        
        return b.getvalue()