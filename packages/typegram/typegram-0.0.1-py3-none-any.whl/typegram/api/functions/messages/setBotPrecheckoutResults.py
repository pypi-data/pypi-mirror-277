
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



class SetBotPrecheckoutResults(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9C2DD95``

query_id (``int`` ``64-bit``):
                    N/A
                
        success (``bool``, *optional*):
                    N/A
                
        error (``str``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "success", "error"]

    ID = 0x9c2dd95
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, query_id: int, success: Optional[bool] = None, error: Optional[str] = None) -> None:
        
                self.query_id = query_id  # long
        
                self.success = success  # true
        
                self.error = error  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotPrecheckoutResults":
        
        flags = Int.read(b)
        
        success = True if flags & (1 << 1) else False
        query_id = Long.read(b)
        
        error = String.read(b) if flags & (1 << 0) else None
        return SetBotPrecheckoutResults(query_id=query_id, success=success, error=error)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        if self.error is not None:
            b.write(String(self.error))
        
        return b.getvalue()