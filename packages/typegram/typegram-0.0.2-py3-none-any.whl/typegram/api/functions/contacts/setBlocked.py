
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



class SetBlocked(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``94C65C76``

id (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        my_stories_from (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "limit", "my_stories_from"]

    ID = 0x94c65c76
    QUALNAME = "functions.contacts.setBlocked"

    def __init__(self, *, id: List["api.ayiin.InputPeer"], limit: int, my_stories_from: Optional[bool] = None) -> None:
        
                self.id = id  # InputPeer
        
                self.limit = limit  # int
        
                self.my_stories_from = my_stories_from  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBlocked":
        
        flags = Int.read(b)
        
        my_stories_from = True if flags & (1 << 0) else False
        id = Object.read(b)
        
        limit = Int.read(b)
        
        return SetBlocked(id=id, limit=limit, my_stories_from=my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()