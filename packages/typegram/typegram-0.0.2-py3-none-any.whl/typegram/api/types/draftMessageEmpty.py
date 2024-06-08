
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



class DraftMessageEmpty(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.DraftMessage`.

    Details:
        - Layer: ``181``
        - ID: ``1B0C841A``

date (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["date"]

    ID = 0x1b0c841a
    QUALNAME = "types.draftMessageEmpty"

    def __init__(self, *, date: Optional[int] = None) -> None:
        
                self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DraftMessageEmpty":
        
        flags = Int.read(b)
        
        date = Int.read(b) if flags & (1 << 0) else None
        return DraftMessageEmpty(date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.date is not None:
            b.write(Int(self.date))
        
        return b.getvalue()