
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



class StoryFwdHeader(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StoryFwdHeader`.

    Details:
        - Layer: ``181``
        - ID: ``B826E150``

modified (``bool``, *optional*):
                    N/A
                
        from_user (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        from_name (``str``, *optional*):
                    N/A
                
        story_id (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["modified", "from_user", "from_name", "story_id"]

    ID = 0xb826e150
    QUALNAME = "types.storyFwdHeader"

    def __init__(self, *, modified: Optional[bool] = None, from_user: "api.ayiin.Peer" = None, from_name: Optional[str] = None, story_id: Optional[int] = None) -> None:
        
                self.modified = modified  # true
        
                self.from_user = from_user  # Peer
        
                self.from_name = from_name  # string
        
                self.story_id = story_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryFwdHeader":
        
        flags = Int.read(b)
        
        modified = True if flags & (1 << 3) else False
        from_user = Object.read(b) if flags & (1 << 0) else None
        
        from_name = String.read(b) if flags & (1 << 1) else None
        story_id = Int.read(b) if flags & (1 << 2) else None
        return StoryFwdHeader(modified=modified, from_user=from_user, from_name=from_name, story_id=story_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.from_user is not None:
            b.write(self.from_user.write())
        
        if self.from_name is not None:
            b.write(String(self.from_name))
        
        if self.story_id is not None:
            b.write(Int(self.story_id))
        
        return b.getvalue()