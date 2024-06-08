
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



class StoryReactionPublicRepost(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StoryReaction`.

    Details:
        - Layer: ``181``
        - ID: ``CFCD0F13``

peer_id (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        story (:obj:`StoryItem<typegram.api.ayiin.StoryItem>`):
                    N/A
                
    """

    __slots__: List[str] = ["peer_id", "story"]

    ID = 0xcfcd0f13
    QUALNAME = "types.storyReactionPublicRepost"

    def __init__(self, *, peer_id: "api.ayiin.Peer", story: "api.ayiin.StoryItem") -> None:
        
                self.peer_id = peer_id  # Peer
        
                self.story = story  # StoryItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryReactionPublicRepost":
        # No flags
        
        peer_id = Object.read(b)
        
        story = Object.read(b)
        
        return StoryReactionPublicRepost(peer_id=peer_id, story=story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer_id.write())
        
        b.write(self.story.write())
        
        return b.getvalue()