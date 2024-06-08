
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



class MessagesSlice(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.Messages`.

    Details:
        - Layer: ``181``
        - ID: ``3A54685E``

count (``int`` ``32-bit``):
                    N/A
                
        messages (List of :obj:`Message<typegram.api.ayiin.Message>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        inexact (``bool``, *optional*):
                    N/A
                
        next_rate (``int`` ``32-bit``, *optional*):
                    N/A
                
        offset_id_offset (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 22 functions.

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

    __slots__: List[str] = ["count", "messages", "chats", "users", "inexact", "next_rate", "offset_id_offset"]

    ID = 0x3a54685e
    QUALNAME = "types.messages.messagesSlice"

    def __init__(self, *, count: int, messages: List["api.ayiin.Message"], chats: List["api.ayiin.Chat"], users: List["api.ayiin.User"], inexact: Optional[bool] = None, next_rate: Optional[int] = None, offset_id_offset: Optional[int] = None) -> None:
        
                self.count = count  # int
        
                self.messages = messages  # Message
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.inexact = inexact  # true
        
                self.next_rate = next_rate  # int
        
                self.offset_id_offset = offset_id_offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessagesSlice":
        
        flags = Int.read(b)
        
        inexact = True if flags & (1 << 1) else False
        count = Int.read(b)
        
        next_rate = Int.read(b) if flags & (1 << 0) else None
        offset_id_offset = Int.read(b) if flags & (1 << 2) else None
        messages = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return MessagesSlice(count=count, messages=messages, chats=chats, users=users, inexact=inexact, next_rate=next_rate, offset_id_offset=offset_id_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        if self.next_rate is not None:
            b.write(Int(self.next_rate))
        
        if self.offset_id_offset is not None:
            b.write(Int(self.offset_id_offset))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()