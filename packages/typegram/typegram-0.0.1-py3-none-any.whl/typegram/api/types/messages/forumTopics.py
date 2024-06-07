
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



class ForumTopics(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.ForumTopics`.

    Details:
        - Layer: ``181``
        - ID: ``367617D3``

count (``int`` ``32-bit``):
                    N/A
                
        topics (List of :obj:`ForumTopic<typegram.api.ayiin.ForumTopic>`):
                    N/A
                
        messages (List of :obj:`Message<typegram.api.ayiin.Message>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        pts (``int`` ``32-bit``):
                    N/A
                
        order_by_create_date (``bool``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.Messages
            messages.Dialogs
            messages.AffectedMessages
            messages.AffectedHistory
            messages.PeerSettings
            messages.Chats
            messages.ChatFull
            messages.InvitedUsers
            messages.DhConfig
            messages.SentEncryptedMessage
            messages.Stickers
            messages.AllStickers
            messages.StickerSet
            messages.StickerSetInstallResult
            messages.MessageViews
            messages.SavedGifs
            messages.BotResults
            messages.MessageEditData
            messages.BotCallbackAnswer
            messages.PeerDialogs
            messages.FeaturedStickers
            messages.RecentStickers
            messages.ArchivedStickers
            messages.HighScores
            messages.WebPage
            messages.FavedStickers
            messages.FoundStickerSets
            Vector<messages.SearchCounter>
            messages.VotesList
            messages.DiscussionMessage
            messages.AffectedFoundMessages
            messages.HistoryImportParsed
            messages.HistoryImport
            messages.ExportedChatInvites
            messages.ExportedChatInvite
            messages.ChatAdminsWithInvites
            messages.ChatInviteImporters
            messages.CheckedHistoryImportPeer
            messages.SearchResultsCalendar
            messages.SearchResultsPositions
            messages.MessageReactionsList
            messages.AvailableReactions
            messages.TranslatedText
            messages.TranscribedAudio
            messages.Reactions
            messages.EmojiGroups
            messages.BotApp
            messages.SavedDialogs
            messages.SavedReactionTags
            messages.QuickReplies
            messages.MyStickers
            messages.AvailableEffects
            messages.SponsoredMessages
            messages.ForumTopics
    """

    __slots__: List[str] = ["count", "topics", "messages", "chats", "users", "pts", "order_by_create_date"]

    ID = 0x367617d3
    QUALNAME = "functions.typesmessages.ForumTopics"

    def __init__(self, *, count: int, topics: List["ayiin.ForumTopic"], messages: List["ayiin.Message"], chats: List["ayiin.Chat"], users: List["ayiin.User"], pts: int, order_by_create_date: Optional[bool] = None) -> None:
        
                self.count = count  # int
        
                self.topics = topics  # ForumTopic
        
                self.messages = messages  # Message
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.pts = pts  # int
        
                self.order_by_create_date = order_by_create_date  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForumTopics":
        
        flags = Int.read(b)
        
        order_by_create_date = True if flags & (1 << 0) else False
        count = Int.read(b)
        
        topics = Object.read(b)
        
        messages = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        pts = Int.read(b)
        
        return ForumTopics(count=count, topics=topics, messages=messages, chats=chats, users=users, pts=pts, order_by_create_date=order_by_create_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.topics))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        b.write(Int(self.pts))
        
        return b.getvalue()