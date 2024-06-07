
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



class ReceivedQueue(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``55A5BB66``

max_qts (``int`` ``32-bit``):
                    N/A
                
    Returns:
        List of ``int`` ``64-bit``
    """

    __slots__: List[str] = ["max_qts"]

    ID = 0x55a5bb66
    QUALNAME = "functions.functions.Vector<long>"

    def __init__(self, *, max_qts: int) -> None:
        
                self.max_qts = max_qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReceivedQueue":
        # No flags
        
        max_qts = Int.read(b)
        
        return ReceivedQueue(max_qts=max_qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.max_qts))
        
        return b.getvalue()