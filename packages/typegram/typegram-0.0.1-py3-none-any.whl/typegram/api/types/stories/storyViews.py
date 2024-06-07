
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



class StoryViews(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stories.StoryViews`.

    Details:
        - Layer: ``181``
        - ID: ``DE9EED1D``

views (List of :obj:`StoryViews<typegram.api.ayiin.StoryViews>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
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

    __slots__: List[str] = ["views", "users"]

    ID = 0xde9eed1d
    QUALNAME = "functions.typesstories.StoryViews"

    def __init__(self, *, views: List["ayiin.StoryViews"], users: List["ayiin.User"]) -> None:
        
                self.views = views  # StoryViews
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViews":
        # No flags
        
        views = Object.read(b)
        
        users = Object.read(b)
        
        return StoryViews(views=views, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.views))
        
        b.write(Vector(self.users))
        
        return b.getvalue()