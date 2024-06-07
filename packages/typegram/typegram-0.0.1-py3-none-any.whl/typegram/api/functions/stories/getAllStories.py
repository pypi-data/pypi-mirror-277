
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



class GetAllStories(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``EEB0D625``

next (``bool``, *optional*):
                    N/A
                
        hidden (``bool``, *optional*):
                    N/A
                
        state (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`stories.AllStories<typegram.api.ayiin.stories.AllStories>`
    """

    __slots__: List[str] = ["next", "hidden", "state"]

    ID = 0xeeb0d625
    QUALNAME = "functions.functionsstories.AllStories"

    def __init__(self, *, next: Optional[bool] = None, hidden: Optional[bool] = None, state: Optional[str] = None) -> None:
        
                self.next = next  # true
        
                self.hidden = hidden  # true
        
                self.state = state  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAllStories":
        
        flags = Int.read(b)
        
        next = True if flags & (1 << 1) else False
        hidden = True if flags & (1 << 2) else False
        state = String.read(b) if flags & (1 << 0) else None
        return GetAllStories(next=next, hidden=hidden, state=state)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.state is not None:
            b.write(String(self.state))
        
        return b.getvalue()