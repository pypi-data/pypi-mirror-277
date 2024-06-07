
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



class Stories(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stories.Stories`.

    Details:
        - Layer: ``181``
        - ID: ``63C3DD0A``

count (``int`` ``32-bit``):
                    N/A
                
        stories (List of :obj:`StoryItem<typegram.api.ayiin.StoryItem>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        pinned_to_top (List of ``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 15 functions.

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

    __slots__: List[str] = ["count", "stories", "chats", "users", "pinned_to_top"]

    ID = 0x63c3dd0a
    QUALNAME = "functions.typesstories.Stories"

    def __init__(self, *, count: int, stories: List["ayiin.StoryItem"], chats: List["ayiin.Chat"], users: List["ayiin.User"], pinned_to_top: Optional[List[int]] = None) -> None:
        
                self.count = count  # int
        
                self.stories = stories  # StoryItem
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.pinned_to_top = pinned_to_top  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Stories":
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        stories = Object.read(b)
        
        pinned_to_top = Object.read(b, Int) if flags & (1 << 0) else []
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return Stories(count=count, stories=stories, chats=chats, users=users, pinned_to_top=pinned_to_top)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.stories))
        
        if self.pinned_to_top is not None:
            b.write(Vector(self.pinned_to_top, Int))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()