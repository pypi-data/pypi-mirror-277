
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



class SendReaction(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``7FD736B2``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        story_id (``int`` ``32-bit``):
                    N/A
                
        reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`):
                    N/A
                
        add_to_recent (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "story_id", "reaction", "add_to_recent"]

    ID = 0x7fd736b2
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", story_id: int, reaction: "ayiin.Reaction", add_to_recent: Optional[bool] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.story_id = story_id  # int
        
                self.reaction = reaction  # Reaction
        
                self.add_to_recent = add_to_recent  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendReaction":
        
        flags = Int.read(b)
        
        add_to_recent = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        story_id = Int.read(b)
        
        reaction = Object.read(b)
        
        return SendReaction(peer=peer, story_id=story_id, reaction=reaction, add_to_recent=add_to_recent)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.story_id))
        
        b.write(self.reaction.write())
        
        return b.getvalue()