
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



class AllStoriesNotModified(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stories.AllStories`.

    Details:
        - Layer: ``181``
        - ID: ``1158FE3E``

state (``str``):
                    N/A
                
        stealth_mode (:obj:`StoriesStealthMode<typegram.api.ayiin.StoriesStealthMode>`):
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

    __slots__: List[str] = ["state", "stealth_mode"]

    ID = 0x1158fe3e
    QUALNAME = "functions.typesstories.AllStories"

    def __init__(self, *, state: str, stealth_mode: "ayiin.StoriesStealthMode") -> None:
        
                self.state = state  # string
        
                self.stealth_mode = stealth_mode  # StoriesStealthMode

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AllStoriesNotModified":
        
        flags = Int.read(b)
        
        state = String.read(b)
        
        stealth_mode = Object.read(b)
        
        return AllStoriesNotModified(state=state, stealth_mode=stealth_mode)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.state))
        
        b.write(self.stealth_mode.write())
        
        return b.getvalue()