
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



class AllStories(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stories.AllStories`.

    Details:
        - Layer: ``181``
        - ID: ``6EFC5E81``

count (``int`` ``32-bit``):
                    N/A
                
        state (``str``):
                    N/A
                
        peer_stories (List of :obj:`PeerStories<typegram.api.ayiin.PeerStories>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        stealth_mode (:obj:`StoriesStealthMode<typegram.api.ayiin.StoriesStealthMode>`):
                    N/A
                
        has_more (``bool``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

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

    __slots__: List[str] = ["count", "state", "peer_stories", "chats", "users", "stealth_mode", "has_more"]

    ID = 0x6efc5e81
    QUALNAME = "functions.typesstories.AllStories"

    def __init__(self, *, count: int, state: str, peer_stories: List["ayiin.PeerStories"], chats: List["ayiin.Chat"], users: List["ayiin.User"], stealth_mode: "ayiin.StoriesStealthMode", has_more: Optional[bool] = None) -> None:
        
                self.count = count  # int
        
                self.state = state  # string
        
                self.peer_stories = peer_stories  # PeerStories
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.stealth_mode = stealth_mode  # StoriesStealthMode
        
                self.has_more = has_more  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AllStories":
        
        flags = Int.read(b)
        
        has_more = True if flags & (1 << 0) else False
        count = Int.read(b)
        
        state = String.read(b)
        
        peer_stories = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        stealth_mode = Object.read(b)
        
        return AllStories(count=count, state=state, peer_stories=peer_stories, chats=chats, users=users, stealth_mode=stealth_mode, has_more=has_more)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(String(self.state))
        
        b.write(Vector(self.peer_stories))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        b.write(self.stealth_mode.write())
        
        return b.getvalue()