
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



class MessageReactionsList(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.MessageReactionsList`.

    Details:
        - Layer: ``181``
        - ID: ``31BD492D``

count (``int`` ``32-bit``):
                    N/A
                
        reactions (List of :obj:`MessagePeerReaction<typegram.api.ayiin.MessagePeerReaction>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        next_offset (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 29 functions.

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

    __slots__: List[str] = ["count", "reactions", "chats", "users", "next_offset"]

    ID = 0x31bd492d
    QUALNAME = "functions.typesmessages.MessageReactionsList"

    def __init__(self, *, count: int, reactions: List["ayiin.MessagePeerReaction"], chats: List["ayiin.Chat"], users: List["ayiin.User"], next_offset: Optional[str] = None) -> None:
        
                self.count = count  # int
        
                self.reactions = reactions  # MessagePeerReaction
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.next_offset = next_offset  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReactionsList":
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        reactions = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        return MessageReactionsList(count=count, reactions=reactions, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.reactions))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        return b.getvalue()