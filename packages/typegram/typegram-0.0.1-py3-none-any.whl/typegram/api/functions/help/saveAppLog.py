
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



class SaveAppLog(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``6F02F748``

events (List of :obj:`InputAppEvent<typegram.api.ayiin.InputAppEvent>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["events"]

    ID = 0x6f02f748
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, events: List["ayiin.InputAppEvent"]) -> None:
        
                self.events = events  # InputAppEvent

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveAppLog":
        # No flags
        
        events = Object.read(b)
        
        return SaveAppLog(events=events)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.events))
        
        return b.getvalue()