
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



class ActivateStealthMode(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``57BBD166``

past (``bool``, *optional*):
                    N/A
                
        future (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["past", "future"]

    ID = 0x57bbd166
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, past: Optional[bool] = None, future: Optional[bool] = None) -> None:
        
                self.past = past  # true
        
                self.future = future  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ActivateStealthMode":
        
        flags = Int.read(b)
        
        past = True if flags & (1 << 0) else False
        future = True if flags & (1 << 1) else False
        return ActivateStealthMode(past=past, future=future)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()