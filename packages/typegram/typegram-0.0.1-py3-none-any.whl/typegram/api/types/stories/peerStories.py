
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



class PeerStories(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stories.PeerStories`.

    Details:
        - Layer: ``181``
        - ID: ``CAE68768``

stories (:obj:`PeerStories<typegram.api.ayiin.PeerStories>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 19 functions.

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

    __slots__: List[str] = ["stories", "chats", "users"]

    ID = 0xcae68768
    QUALNAME = "functions.typesstories.PeerStories"

    def __init__(self, *, stories: "ayiin.PeerStories", chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.stories = stories  # PeerStories
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerStories":
        # No flags
        
        stories = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return PeerStories(stories=stories, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stories.write())
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()