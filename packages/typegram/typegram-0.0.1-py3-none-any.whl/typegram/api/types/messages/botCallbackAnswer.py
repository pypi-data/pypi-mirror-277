
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



class BotCallbackAnswer(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.BotCallbackAnswer`.

    Details:
        - Layer: ``181``
        - ID: ``36585EA4``

cache_time (``int`` ``32-bit``):
                    N/A
                
        alert (``bool``, *optional*):
                    N/A
                
        has_url (``bool``, *optional*):
                    N/A
                
        native_ui (``bool``, *optional*):
                    N/A
                
        message (``str``, *optional*):
                    N/A
                
        url (``str``, *optional*):
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

    __slots__: List[str] = ["cache_time", "alert", "has_url", "native_ui", "message", "url"]

    ID = 0x36585ea4
    QUALNAME = "functions.typesmessages.BotCallbackAnswer"

    def __init__(self, *, cache_time: int, alert: Optional[bool] = None, has_url: Optional[bool] = None, native_ui: Optional[bool] = None, message: Optional[str] = None, url: Optional[str] = None) -> None:
        
                self.cache_time = cache_time  # int
        
                self.alert = alert  # true
        
                self.has_url = has_url  # true
        
                self.native_ui = native_ui  # true
        
                self.message = message  # string
        
                self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCallbackAnswer":
        
        flags = Int.read(b)
        
        alert = True if flags & (1 << 1) else False
        has_url = True if flags & (1 << 3) else False
        native_ui = True if flags & (1 << 4) else False
        message = String.read(b) if flags & (1 << 0) else None
        url = String.read(b) if flags & (1 << 2) else None
        cache_time = Int.read(b)
        
        return BotCallbackAnswer(cache_time=cache_time, alert=alert, has_url=has_url, native_ui=native_ui, message=message, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.url is not None:
            b.write(String(self.url))
        
        b.write(Int(self.cache_time))
        
        return b.getvalue()