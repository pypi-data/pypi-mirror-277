
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



class Unblock(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B550D328``

id (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        my_stories_from (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "my_stories_from"]

    ID = 0xb550d328
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, id: "ayiin.InputPeer", my_stories_from: Optional[bool] = None) -> None:
        
                self.id = id  # InputPeer
        
                self.my_stories_from = my_stories_from  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Unblock":
        
        flags = Int.read(b)
        
        my_stories_from = True if flags & (1 << 0) else False
        id = Object.read(b)
        
        return Unblock(id=id, my_stories_from=my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        return b.getvalue()