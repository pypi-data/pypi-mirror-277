
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



class PublicForwards(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stats.PublicForwards`.

    Details:
        - Layer: ``181``
        - ID: ``93037E20``

count (``int`` ``32-bit``):
                    N/A
                
        forwards (List of :obj:`PublicForward<typegram.api.ayiin.PublicForward>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        next_offset (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            stats.BroadcastStats
            stats.MegagroupStats
            stats.PublicForwards
            stats.MessageStats
            stats.StoryStats
            stats.BroadcastRevenueStats
            stats.BroadcastRevenueWithdrawalUrl
            stats.BroadcastRevenueTransactions
    """

    __slots__: List[str] = ["count", "forwards", "chats", "users", "next_offset"]

    ID = 0x93037e20
    QUALNAME = "functions.typesstats.PublicForwards"

    def __init__(self, *, count: int, forwards: List["ayiin.PublicForward"], chats: List["ayiin.Chat"], users: List["ayiin.User"], next_offset: Optional[str] = None) -> None:
        
                self.count = count  # int
        
                self.forwards = forwards  # PublicForward
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.next_offset = next_offset  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PublicForwards":
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        forwards = Object.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return PublicForwards(count=count, forwards=forwards, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.forwards))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()