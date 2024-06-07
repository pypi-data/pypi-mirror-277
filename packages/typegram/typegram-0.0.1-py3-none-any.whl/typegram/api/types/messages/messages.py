
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



class Messages(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.Messages`.

    Details:
        - Layer: ``181``
        - ID: ``8C718E87``

messages (List of :obj:`Message<typegram.api.ayiin.Message>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

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

    __slots__: List[str] = ["messages", "chats", "users"]

    ID = 0x8c718e87
    QUALNAME = "functions.typesmessages.Messages"

    def __init__(self, *, messages: List["ayiin.Message"], chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.messages = messages  # Message
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Messages":
        # No flags
        
        messages = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return Messages(messages=messages, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()