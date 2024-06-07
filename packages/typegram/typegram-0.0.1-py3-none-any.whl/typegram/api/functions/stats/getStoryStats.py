
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



class GetStoryStats(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``374FEF40``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        dark (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`stats.StoryStats<typegram.api.ayiin.stats.StoryStats>`
    """

    __slots__: List[str] = ["peer", "id", "dark"]

    ID = 0x374fef40
    QUALNAME = "functions.functionsstats.StoryStats"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int, dark: Optional[bool] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.dark = dark  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryStats":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        id = Int.read(b)
        
        return GetStoryStats(peer=peer, id=id, dark=dark)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()