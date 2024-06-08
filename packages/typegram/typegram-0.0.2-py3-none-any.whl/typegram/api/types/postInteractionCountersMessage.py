
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



class PostInteractionCountersMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PostInteractionCounters`.

    Details:
        - Layer: ``181``
        - ID: ``E7058E7F``

msg_id (``int`` ``32-bit``):
                    N/A
                
        views (``int`` ``32-bit``):
                    N/A
                
        forwards (``int`` ``32-bit``):
                    N/A
                
        reactions (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["msg_id", "views", "forwards", "reactions"]

    ID = 0xe7058e7f
    QUALNAME = "types.postInteractionCountersMessage"

    def __init__(self, *, msg_id: int, views: int, forwards: int, reactions: int) -> None:
        
                self.msg_id = msg_id  # int
        
                self.views = views  # int
        
                self.forwards = forwards  # int
        
                self.reactions = reactions  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PostInteractionCountersMessage":
        # No flags
        
        msg_id = Int.read(b)
        
        views = Int.read(b)
        
        forwards = Int.read(b)
        
        reactions = Int.read(b)
        
        return PostInteractionCountersMessage(msg_id=msg_id, views=views, forwards=forwards, reactions=reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.views))
        
        b.write(Int(self.forwards))
        
        b.write(Int(self.reactions))
        
        return b.getvalue()