
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



class SetBotCallbackAnswer(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D58F130A``

query_id (``int`` ``64-bit``):
                    N/A
                
        cache_time (``int`` ``32-bit``):
                    N/A
                
        alert (``bool``, *optional*):
                    N/A
                
        message (``str``, *optional*):
                    N/A
                
        url (``str``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "cache_time", "alert", "message", "url"]

    ID = 0xd58f130a
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, query_id: int, cache_time: int, alert: Optional[bool] = None, message: Optional[str] = None, url: Optional[str] = None) -> None:
        
                self.query_id = query_id  # long
        
                self.cache_time = cache_time  # int
        
                self.alert = alert  # true
        
                self.message = message  # string
        
                self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotCallbackAnswer":
        
        flags = Int.read(b)
        
        alert = True if flags & (1 << 1) else False
        query_id = Long.read(b)
        
        message = String.read(b) if flags & (1 << 0) else None
        url = String.read(b) if flags & (1 << 2) else None
        cache_time = Int.read(b)
        
        return SetBotCallbackAnswer(query_id=query_id, cache_time=cache_time, alert=alert, message=message, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.url is not None:
            b.write(String(self.url))
        
        b.write(Int(self.cache_time))
        
        return b.getvalue()