
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



class StoryViewPublicForward(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StoryView`.

    Details:
        - Layer: ``181``
        - ID: ``9083670B``

message (:obj:`Message<typegram.api.ayiin.Message>`):
                    N/A
                
        blocked (``bool``, *optional*):
                    N/A
                
        blocked_my_stories_from (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["message", "blocked", "blocked_my_stories_from"]

    ID = 0x9083670b
    QUALNAME = "types.storyViewPublicForward"

    def __init__(self, *, message: "api.ayiin.Message", blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None) -> None:
        
                self.message = message  # Message
        
                self.blocked = blocked  # true
        
                self.blocked_my_stories_from = blocked_my_stories_from  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViewPublicForward":
        
        flags = Int.read(b)
        
        blocked = True if flags & (1 << 0) else False
        blocked_my_stories_from = True if flags & (1 << 1) else False
        message = Object.read(b)
        
        return StoryViewPublicForward(message=message, blocked=blocked, blocked_my_stories_from=blocked_my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.message.write())
        
        return b.getvalue()