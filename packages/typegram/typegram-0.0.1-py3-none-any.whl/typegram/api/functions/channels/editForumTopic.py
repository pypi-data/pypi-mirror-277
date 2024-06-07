
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



class EditForumTopic(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F4DFA185``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        topic_id (``int`` ``32-bit``):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        icon_emoji_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        closed (``bool``, *optional*):
                    N/A
                
        hidden (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["channel", "topic_id", "title", "icon_emoji_id", "closed", "hidden"]

    ID = 0xf4dfa185
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, channel: "ayiin.InputChannel", topic_id: int, title: Optional[str] = None, icon_emoji_id: Optional[int] = None, closed: Optional[bool] = None, hidden: Optional[bool] = None) -> None:
        
                self.channel = channel  # InputChannel
        
                self.topic_id = topic_id  # int
        
                self.title = title  # string
        
                self.icon_emoji_id = icon_emoji_id  # long
        
                self.closed = closed  # Bool
        
                self.hidden = hidden  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditForumTopic":
        
        flags = Int.read(b)
        
        channel = Object.read(b)
        
        topic_id = Int.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        icon_emoji_id = Long.read(b) if flags & (1 << 1) else None
        closed = Bool.read(b) if flags & (1 << 2) else None
        hidden = Bool.read(b) if flags & (1 << 3) else None
        return EditForumTopic(channel=channel, topic_id=topic_id, title=title, icon_emoji_id=icon_emoji_id, closed=closed, hidden=hidden)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.topic_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        if self.closed is not None:
            b.write(Bool(self.closed))
        
        if self.hidden is not None:
            b.write(Bool(self.hidden))
        
        return b.getvalue()