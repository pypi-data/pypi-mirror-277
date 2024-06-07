
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



class GetRecentStickers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9DA9403B``

hash (``int`` ``64-bit``):
                    N/A
                
        attached (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.RecentStickers<typegram.api.ayiin.messages.RecentStickers>`
    """

    __slots__: List[str] = ["hash", "attached"]

    ID = 0x9da9403b
    QUALNAME = "functions.functionsmessages.RecentStickers"

    def __init__(self, *, hash: int, attached: Optional[bool] = None) -> None:
        
                self.hash = hash  # long
        
                self.attached = attached  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentStickers":
        
        flags = Int.read(b)
        
        attached = True if flags & (1 << 0) else False
        hash = Long.read(b)
        
        return GetRecentStickers(hash=hash, attached=attached)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.hash))
        
        return b.getvalue()