
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



class UpdateNewStoryReaction(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``1824E40B``

story_id (``int`` ``32-bit``):
                    N/A
                
        peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`):
                    N/A
                
    """

    __slots__: List[str] = ["story_id", "peer", "reaction"]

    ID = 0x1824e40b
    QUALNAME = "types.updateNewStoryReaction"

    def __init__(self, *, story_id: int, peer: "api.ayiin.Peer", reaction: "api.ayiin.Reaction") -> None:
        
                self.story_id = story_id  # int
        
                self.peer = peer  # Peer
        
                self.reaction = reaction  # Reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewStoryReaction":
        # No flags
        
        story_id = Int.read(b)
        
        peer = Object.read(b)
        
        reaction = Object.read(b)
        
        return UpdateNewStoryReaction(story_id=story_id, peer=peer, reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.story_id))
        
        b.write(self.peer.write())
        
        b.write(self.reaction.write())
        
        return b.getvalue()