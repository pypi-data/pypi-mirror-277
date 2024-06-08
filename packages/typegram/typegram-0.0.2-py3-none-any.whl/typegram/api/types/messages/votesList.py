
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



class VotesList(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.VotesList`.

    Details:
        - Layer: ``181``
        - ID: ``4899484E``

count (``int`` ``32-bit``):
                    N/A
                
        votes (List of :obj:`MessagePeerVote<typegram.api.ayiin.MessagePeerVote>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        next_offset (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getPollVotes
    """

    __slots__: List[str] = ["count", "votes", "chats", "users", "next_offset"]

    ID = 0x4899484e
    QUALNAME = "types.messages.votesList"

    def __init__(self, *, count: int, votes: List["api.ayiin.MessagePeerVote"], chats: List["api.ayiin.Chat"], users: List["api.ayiin.User"], next_offset: Optional[str] = None) -> None:
        
                self.count = count  # int
        
                self.votes = votes  # MessagePeerVote
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.next_offset = next_offset  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VotesList":
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        votes = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        return VotesList(count=count, votes=votes, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.votes))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        return b.getvalue()