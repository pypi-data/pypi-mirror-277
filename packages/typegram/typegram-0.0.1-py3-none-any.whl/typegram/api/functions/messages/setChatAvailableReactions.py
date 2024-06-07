
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



class SetChatAvailableReactions(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``5A150BD4``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        available_reactions (:obj:`ChatReactions<typegram.api.ayiin.ChatReactions>`):
                    N/A
                
        reactions_limit (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "available_reactions", "reactions_limit"]

    ID = 0x5a150bd4
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", available_reactions: "ayiin.ChatReactions", reactions_limit: Optional[int] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.available_reactions = available_reactions  # ChatReactions
        
                self.reactions_limit = reactions_limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetChatAvailableReactions":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        available_reactions = Object.read(b)
        
        reactions_limit = Int.read(b) if flags & (1 << 0) else None
        return SetChatAvailableReactions(peer=peer, available_reactions=available_reactions, reactions_limit=reactions_limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.available_reactions.write())
        
        if self.reactions_limit is not None:
            b.write(Int(self.reactions_limit))
        
        return b.getvalue()