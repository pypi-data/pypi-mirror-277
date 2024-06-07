
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



class SearchResultsCalendar(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.SearchResultsCalendar`.

    Details:
        - Layer: ``181``
        - ID: ``147EE23C``

count (``int`` ``32-bit``):
                    N/A
                
        min_date (``int`` ``32-bit``):
                    N/A
                
        min_msg_id (``int`` ``32-bit``):
                    N/A
                
        periods (List of :obj:`SearchResultsCalendarPeriod<typegram.api.ayiin.SearchResultsCalendarPeriod>`):
                    N/A
                
        messages (List of :obj:`Message<typegram.api.ayiin.Message>`):
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
        This object can be returned by 30 functions.

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

    __slots__: List[str] = ["count", "min_date", "min_msg_id", "periods", "messages", "chats", "users", "inexact", "offset_id_offset"]

    ID = 0x147ee23c
    QUALNAME = "functions.typesmessages.SearchResultsCalendar"

    def __init__(self, *, count: int, min_date: int, min_msg_id: int, periods: List["ayiin.SearchResultsCalendarPeriod"], messages: List["ayiin.Message"], chats: List["ayiin.Chat"], users: List["ayiin.User"], inexact: Optional[bool] = None, offset_id_offset: Optional[int] = None) -> None:
        
                self.count = count  # int
        
                self.min_date = min_date  # int
        
                self.min_msg_id = min_msg_id  # int
        
                self.periods = periods  # SearchResultsCalendarPeriod
        
                self.messages = messages  # Message
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.inexact = inexact  # true
        
                self.offset_id_offset = offset_id_offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchResultsCalendar":
        
        flags = Int.read(b)
        
        inexact = True if flags & (1 << 0) else False
        count = Int.read(b)
        
        min_date = Int.read(b)
        
        min_msg_id = Int.read(b)
        
        offset_id_offset = Int.read(b) if flags & (1 << 1) else None
        periods = Object.read(b)
        
        messages = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return SearchResultsCalendar(count=count, min_date=min_date, min_msg_id=min_msg_id, periods=periods, messages=messages, chats=chats, users=users, inexact=inexact, offset_id_offset=offset_id_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Int(self.min_date))
        
        b.write(Int(self.min_msg_id))
        
        if self.offset_id_offset is not None:
            b.write(Int(self.offset_id_offset))
        
        b.write(Vector(self.periods))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()