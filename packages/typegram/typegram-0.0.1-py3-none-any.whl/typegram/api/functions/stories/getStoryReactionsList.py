
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



class GetStoryReactionsList(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B9B2881F``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        forwards_first (``bool``, *optional*):
                    N/A
                
        reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`, *optional*):
                    N/A
                
        offset (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`stories.StoryReactionsList<typegram.api.ayiin.stories.StoryReactionsList>`
    """

    __slots__: List[str] = ["peer", "id", "limit", "forwards_first", "reaction", "offset"]

    ID = 0xb9b2881f
    QUALNAME = "functions.functionsstories.StoryReactionsList"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int, limit: int, forwards_first: Optional[bool] = None, reaction: "ayiin.Reaction" = None, offset: Optional[str] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.limit = limit  # int
        
                self.forwards_first = forwards_first  # true
        
                self.reaction = reaction  # Reaction
        
                self.offset = offset  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryReactionsList":
        
        flags = Int.read(b)
        
        forwards_first = True if flags & (1 << 2) else False
        peer = Object.read(b)
        
        id = Int.read(b)
        
        reaction = Object.read(b) if flags & (1 << 0) else None
        
        offset = String.read(b) if flags & (1 << 1) else None
        limit = Int.read(b)
        
        return GetStoryReactionsList(peer=peer, id=id, limit=limit, forwards_first=forwards_first, reaction=reaction, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.reaction is not None:
            b.write(self.reaction.write())
        
        if self.offset is not None:
            b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()