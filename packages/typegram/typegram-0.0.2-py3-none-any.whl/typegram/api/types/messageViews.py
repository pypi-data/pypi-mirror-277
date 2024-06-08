
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



class MessageViews(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageViews`.

    Details:
        - Layer: ``181``
        - ID: ``455B853D``

views (``int`` ``32-bit``, *optional*):
                    N/A
                
        forwards (``int`` ``32-bit``, *optional*):
                    N/A
                
        replies (:obj:`MessageReplies<typegram.api.ayiin.MessageReplies>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["views", "forwards", "replies"]

    ID = 0x455b853d
    QUALNAME = "types.messageViews"

    def __init__(self, *, views: Optional[int] = None, forwards: Optional[int] = None, replies: "api.ayiin.MessageReplies" = None) -> None:
        
                self.views = views  # int
        
                self.forwards = forwards  # int
        
                self.replies = replies  # MessageReplies

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageViews":
        
        flags = Int.read(b)
        
        views = Int.read(b) if flags & (1 << 0) else None
        forwards = Int.read(b) if flags & (1 << 1) else None
        replies = Object.read(b) if flags & (1 << 2) else None
        
        return MessageViews(views=views, forwards=forwards, replies=replies)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.views is not None:
            b.write(Int(self.views))
        
        if self.forwards is not None:
            b.write(Int(self.forwards))
        
        if self.replies is not None:
            b.write(self.replies.write())
        
        return b.getvalue()