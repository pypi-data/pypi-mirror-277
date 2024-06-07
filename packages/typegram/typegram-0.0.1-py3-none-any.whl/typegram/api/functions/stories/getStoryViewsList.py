
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



class GetStoryViewsList(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``7ED23C57``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        offset (``str``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        just_contacts (``bool``, *optional*):
                    N/A
                
        reactions_first (``bool``, *optional*):
                    N/A
                
        forwards_first (``bool``, *optional*):
                    N/A
                
        q (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`stories.StoryViewsList<typegram.api.ayiin.stories.StoryViewsList>`
    """

    __slots__: List[str] = ["peer", "id", "offset", "limit", "just_contacts", "reactions_first", "forwards_first", "q"]

    ID = 0x7ed23c57
    QUALNAME = "functions.functionsstories.StoryViewsList"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int, offset: str, limit: int, just_contacts: Optional[bool] = None, reactions_first: Optional[bool] = None, forwards_first: Optional[bool] = None, q: Optional[str] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.offset = offset  # string
        
                self.limit = limit  # int
        
                self.just_contacts = just_contacts  # true
        
                self.reactions_first = reactions_first  # true
        
                self.forwards_first = forwards_first  # true
        
                self.q = q  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryViewsList":
        
        flags = Int.read(b)
        
        just_contacts = True if flags & (1 << 0) else False
        reactions_first = True if flags & (1 << 2) else False
        forwards_first = True if flags & (1 << 3) else False
        peer = Object.read(b)
        
        q = String.read(b) if flags & (1 << 1) else None
        id = Int.read(b)
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        return GetStoryViewsList(peer=peer, id=id, offset=offset, limit=limit, just_contacts=just_contacts, reactions_first=reactions_first, forwards_first=forwards_first, q=q)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.q is not None:
            b.write(String(self.q))
        
        b.write(Int(self.id))
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()