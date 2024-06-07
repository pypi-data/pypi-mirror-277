
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



class StoryViewsList(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stories.StoryViewsList`.

    Details:
        - Layer: ``181``
        - ID: ``59D78FC5``

count (``int`` ``32-bit``):
                    N/A
                
        views_count (``int`` ``32-bit``):
                    N/A
                
        forwards_count (``int`` ``32-bit``):
                    N/A
                
        reactions_count (``int`` ``32-bit``):
                    N/A
                
        views (List of :obj:`StoryView<typegram.api.ayiin.StoryView>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        next_offset (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 22 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            stories.AllStories
            stories.Stories
            stories.StoryViewsList
            stories.StoryViews
            stories.PeerStories
            stories.StoryReactionsList
    """

    __slots__: List[str] = ["count", "views_count", "forwards_count", "reactions_count", "views", "chats", "users", "next_offset"]

    ID = 0x59d78fc5
    QUALNAME = "functions.typesstories.StoryViewsList"

    def __init__(self, *, count: int, views_count: int, forwards_count: int, reactions_count: int, views: List["ayiin.StoryView"], chats: List["ayiin.Chat"], users: List["ayiin.User"], next_offset: Optional[str] = None) -> None:
        
                self.count = count  # int
        
                self.views_count = views_count  # int
        
                self.forwards_count = forwards_count  # int
        
                self.reactions_count = reactions_count  # int
        
                self.views = views  # StoryView
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.next_offset = next_offset  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViewsList":
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        views_count = Int.read(b)
        
        forwards_count = Int.read(b)
        
        reactions_count = Int.read(b)
        
        views = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        return StoryViewsList(count=count, views_count=views_count, forwards_count=forwards_count, reactions_count=reactions_count, views=views, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Int(self.views_count))
        
        b.write(Int(self.forwards_count))
        
        b.write(Int(self.reactions_count))
        
        b.write(Vector(self.views))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        return b.getvalue()