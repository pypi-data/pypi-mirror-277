
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



class GetMessageReactionsList(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``461B3F48``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`, *optional*):
                    N/A
                
        offset (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.MessageReactionsList<typegram.api.ayiin.messages.MessageReactionsList>`
    """

    __slots__: List[str] = ["peer", "id", "limit", "reaction", "offset"]

    ID = 0x461b3f48
    QUALNAME = "functions.functionsmessages.MessageReactionsList"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int, limit: int, reaction: "ayiin.Reaction" = None, offset: Optional[str] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.limit = limit  # int
        
                self.reaction = reaction  # Reaction
        
                self.offset = offset  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessageReactionsList":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        id = Int.read(b)
        
        reaction = Object.read(b) if flags & (1 << 0) else None
        
        offset = String.read(b) if flags & (1 << 1) else None
        limit = Int.read(b)
        
        return GetMessageReactionsList(peer=peer, id=id, limit=limit, reaction=reaction, offset=offset)

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