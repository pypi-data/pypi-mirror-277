
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



class LoadAsyncGraph(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``621D5FA0``

token (``str``):
                    N/A
                
        x (``int`` ``64-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`
    """

    __slots__: List[str] = ["token", "x"]

    ID = 0x621d5fa0
    QUALNAME = "functions.functions.StatsGraph"

    def __init__(self, *, token: str, x: Optional[int] = None) -> None:
        
                self.token = token  # string
        
                self.x = x  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LoadAsyncGraph":
        
        flags = Int.read(b)
        
        token = String.read(b)
        
        x = Long.read(b) if flags & (1 << 0) else None
        return LoadAsyncGraph(token=token, x=x)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.token))
        
        if self.x is not None:
            b.write(Long(self.x))
        
        return b.getvalue()