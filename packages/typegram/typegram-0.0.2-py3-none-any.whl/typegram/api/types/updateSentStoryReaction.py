
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



class UpdateSentStoryReaction(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``7D627683``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        story_id (``int`` ``32-bit``):
                    N/A
                
        reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "story_id", "reaction"]

    ID = 0x7d627683
    QUALNAME = "types.updateSentStoryReaction"

    def __init__(self, *, peer: "api.ayiin.Peer", story_id: int, reaction: "api.ayiin.Reaction") -> None:
        
                self.peer = peer  # Peer
        
                self.story_id = story_id  # int
        
                self.reaction = reaction  # Reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSentStoryReaction":
        # No flags
        
        peer = Object.read(b)
        
        story_id = Int.read(b)
        
        reaction = Object.read(b)
        
        return UpdateSentStoryReaction(peer=peer, story_id=story_id, reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.story_id))
        
        b.write(self.reaction.write())
        
        return b.getvalue()