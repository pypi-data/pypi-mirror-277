
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



class ChannelMessages(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.Messages`.

    Details:
        - Layer: ``181``
        - ID: ``C776BA4E``

pts (``int`` ``32-bit``):
                    N/A
                
        count (``int`` ``32-bit``):
                    N/A
                
        messages (List of :obj:`Message<typegram.api.ayiin.Message>`):
                    N/A
                
        topics (List of :obj:`ForumTopic<typegram.api.ayiin.ForumTopic>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        inexact (``bool``, *optional*):
                    N/A
                
        offset_id_offset (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 24 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getMessages
            messages.getHistory
            messages.search
            messages.searchGlobal
            messages.getUnreadMentions
            messages.getRecentLocations
            messages.getScheduledHistory
            messages.getScheduledMessages
            messages.getReplies
            messages.getUnreadReactions
            messages.searchSentMedia
            messages.getSavedHistory
            messages.getQuickReplyMessages
            channels.getMessages
            channels.searchPosts
    """

    __slots__: List[str] = ["pts", "count", "messages", "topics", "chats", "users", "inexact", "offset_id_offset"]

    ID = 0xc776ba4e
    QUALNAME = "types.messages.channelMessages"

    def __init__(self, *, pts: int, count: int, messages: List["api.ayiin.Message"], topics: List["api.ayiin.ForumTopic"], chats: List["api.ayiin.Chat"], users: List["api.ayiin.User"], inexact: Optional[bool] = None, offset_id_offset: Optional[int] = None) -> None:
        
                self.pts = pts  # int
        
                self.count = count  # int
        
                self.messages = messages  # Message
        
                self.topics = topics  # ForumTopic
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.inexact = inexact  # true
        
                self.offset_id_offset = offset_id_offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelMessages":
        
        flags = Int.read(b)
        
        inexact = True if flags & (1 << 1) else False
        pts = Int.read(b)
        
        count = Int.read(b)
        
        offset_id_offset = Int.read(b) if flags & (1 << 2) else None
        messages = Object.read(b)
        
        topics = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return ChannelMessages(pts=pts, count=count, messages=messages, topics=topics, chats=chats, users=users, inexact=inexact, offset_id_offset=offset_id_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.count))
        
        if self.offset_id_offset is not None:
            b.write(Int(self.offset_id_offset))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.topics))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()