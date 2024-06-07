
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



class GetBlocked(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9A868F80``

offset (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        my_stories_from (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`contacts.Blocked<typegram.api.ayiin.contacts.Blocked>`
    """

    __slots__: List[str] = ["offset", "limit", "my_stories_from"]

    ID = 0x9a868f80
    QUALNAME = "functions.functionscontacts.Blocked"

    def __init__(self, *, offset: int, limit: int, my_stories_from: Optional[bool] = None) -> None:
        
                self.offset = offset  # int
        
                self.limit = limit  # int
        
                self.my_stories_from = my_stories_from  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBlocked":
        
        flags = Int.read(b)
        
        my_stories_from = True if flags & (1 << 0) else False
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        return GetBlocked(offset=offset, limit=limit, my_stories_from=my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()