
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



class PeerStories(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PeerStories`.

    Details:
        - Layer: ``181``
        - ID: ``9A35E999``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        stories (List of :obj:`StoryItem<typegram.api.ayiin.StoryItem>`):
                    N/A
                
        max_read_id (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "stories", "max_read_id"]

    ID = 0x9a35e999
    QUALNAME = "types.peerStories"

    def __init__(self, *, peer: "api.ayiin.Peer", stories: List["api.ayiin.StoryItem"], max_read_id: Optional[int] = None) -> None:
        
                self.peer = peer  # Peer
        
                self.stories = stories  # StoryItem
        
                self.max_read_id = max_read_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerStories":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        max_read_id = Int.read(b) if flags & (1 << 0) else None
        stories = Object.read(b)
        
        return PeerStories(peer=peer, stories=stories, max_read_id=max_read_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.max_read_id is not None:
            b.write(Int(self.max_read_id))
        
        b.write(Vector(self.stories))
        
        return b.getvalue()