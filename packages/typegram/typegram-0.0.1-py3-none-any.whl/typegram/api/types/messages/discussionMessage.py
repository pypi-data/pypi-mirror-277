
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



class DiscussionMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.DiscussionMessage`.

    Details:
        - Layer: ``181``
        - ID: ``A6341782``

messages (List of :obj:`Message<typegram.api.ayiin.Message>`):
                    N/A
                
        unread_count (``int`` ``32-bit``):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        max_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        read_inbox_max_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        read_outbox_max_id (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 26 functions.

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

    __slots__: List[str] = ["messages", "unread_count", "chats", "users", "max_id", "read_inbox_max_id", "read_outbox_max_id"]

    ID = 0xa6341782
    QUALNAME = "functions.typesmessages.DiscussionMessage"

    def __init__(self, *, messages: List["ayiin.Message"], unread_count: int, chats: List["ayiin.Chat"], users: List["ayiin.User"], max_id: Optional[int] = None, read_inbox_max_id: Optional[int] = None, read_outbox_max_id: Optional[int] = None) -> None:
        
                self.messages = messages  # Message
        
                self.unread_count = unread_count  # int
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.max_id = max_id  # int
        
                self.read_inbox_max_id = read_inbox_max_id  # int
        
                self.read_outbox_max_id = read_outbox_max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DiscussionMessage":
        
        flags = Int.read(b)
        
        messages = Object.read(b)
        
        max_id = Int.read(b) if flags & (1 << 0) else None
        read_inbox_max_id = Int.read(b) if flags & (1 << 1) else None
        read_outbox_max_id = Int.read(b) if flags & (1 << 2) else None
        unread_count = Int.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return DiscussionMessage(messages=messages, unread_count=unread_count, chats=chats, users=users, max_id=max_id, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.messages))
        
        if self.max_id is not None:
            b.write(Int(self.max_id))
        
        if self.read_inbox_max_id is not None:
            b.write(Int(self.read_inbox_max_id))
        
        if self.read_outbox_max_id is not None:
            b.write(Int(self.read_outbox_max_id))
        
        b.write(Int(self.unread_count))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()