
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



class PublicForwardStory(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PublicForward`.

    Details:
        - Layer: ``181``
        - ID: ``EDF3ADD0``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        story (:obj:`StoryItem<typegram.api.ayiin.StoryItem>`):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "story"]

    ID = 0xedf3add0
    QUALNAME = "types.publicForwardStory"

    def __init__(self, *, peer: "api.ayiin.Peer", story: "api.ayiin.StoryItem") -> None:
        
                self.peer = peer  # Peer
        
                self.story = story  # StoryItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PublicForwardStory":
        # No flags
        
        peer = Object.read(b)
        
        story = Object.read(b)
        
        return PublicForwardStory(peer=peer, story=story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.story.write())
        
        return b.getvalue()