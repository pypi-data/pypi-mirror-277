
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



class StoryReaction(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StoryReaction`.

    Details:
        - Layer: ``181``
        - ID: ``6090D6D5``

peer_id (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`):
                    N/A
                
    """

    __slots__: List[str] = ["peer_id", "date", "reaction"]

    ID = 0x6090d6d5
    QUALNAME = "types.storyReaction"

    def __init__(self, *, peer_id: "api.ayiin.Peer", date: int, reaction: "api.ayiin.Reaction") -> None:
        
                self.peer_id = peer_id  # Peer
        
                self.date = date  # int
        
                self.reaction = reaction  # Reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryReaction":
        # No flags
        
        peer_id = Object.read(b)
        
        date = Int.read(b)
        
        reaction = Object.read(b)
        
        return StoryReaction(peer_id=peer_id, date=date, reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer_id.write())
        
        b.write(Int(self.date))
        
        b.write(self.reaction.write())
        
        return b.getvalue()