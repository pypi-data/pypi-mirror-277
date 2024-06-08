
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



class WebPageAttributeStory(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WebPageAttribute`.

    Details:
        - Layer: ``181``
        - ID: ``2E94C3E7``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        story (:obj:`StoryItem<typegram.api.ayiin.StoryItem>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "id", "story"]

    ID = 0x2e94c3e7
    QUALNAME = "types.webPageAttributeStory"

    def __init__(self, *, peer: "api.ayiin.Peer", id: int, story: "api.ayiin.StoryItem" = None) -> None:
        
                self.peer = peer  # Peer
        
                self.id = id  # int
        
                self.story = story  # StoryItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeStory":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        id = Int.read(b)
        
        story = Object.read(b) if flags & (1 << 0) else None
        
        return WebPageAttributeStory(peer=peer, id=id, story=story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.story is not None:
            b.write(self.story.write())
        
        return b.getvalue()