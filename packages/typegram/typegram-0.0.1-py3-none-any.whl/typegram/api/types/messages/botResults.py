
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



class BotResults(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.BotResults`.

    Details:
        - Layer: ``181``
        - ID: ``E021F2F6``

query_id (``int`` ``64-bit``):
                    N/A
                
        results (List of :obj:`BotInlineResult<typegram.api.ayiin.BotInlineResult>`):
                    N/A
                
        cache_time (``int`` ``32-bit``):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        gallery (``bool``, *optional*):
                    N/A
                
        next_offset (``str``, *optional*):
                    N/A
                
        switch_pm (:obj:`InlineBotSwitchPM<typegram.api.ayiin.InlineBotSwitchPM>`, *optional*):
                    N/A
                
        switch_webview (:obj:`InlineBotWebView<typegram.api.ayiin.InlineBotWebView>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 19 functions.

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

    __slots__: List[str] = ["query_id", "results", "cache_time", "users", "gallery", "next_offset", "switch_pm", "switch_webview"]

    ID = 0xe021f2f6
    QUALNAME = "functions.typesmessages.BotResults"

    def __init__(self, *, query_id: int, results: List["ayiin.BotInlineResult"], cache_time: int, users: List["ayiin.User"], gallery: Optional[bool] = None, next_offset: Optional[str] = None, switch_pm: "ayiin.InlineBotSwitchPM" = None, switch_webview: "ayiin.InlineBotWebView" = None) -> None:
        
                self.query_id = query_id  # long
        
                self.results = results  # BotInlineResult
        
                self.cache_time = cache_time  # int
        
                self.users = users  # User
        
                self.gallery = gallery  # true
        
                self.next_offset = next_offset  # string
        
                self.switch_pm = switch_pm  # InlineBotSwitchPM
        
                self.switch_webview = switch_webview  # InlineBotWebView

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotResults":
        
        flags = Int.read(b)
        
        gallery = True if flags & (1 << 0) else False
        query_id = Long.read(b)
        
        next_offset = String.read(b) if flags & (1 << 1) else None
        switch_pm = Object.read(b) if flags & (1 << 2) else None
        
        switch_webview = Object.read(b) if flags & (1 << 3) else None
        
        results = Object.read(b)
        
        cache_time = Int.read(b)
        
        users = Object.read(b)
        
        return BotResults(query_id=query_id, results=results, cache_time=cache_time, users=users, gallery=gallery, next_offset=next_offset, switch_pm=switch_pm, switch_webview=switch_webview)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        if self.switch_pm is not None:
            b.write(self.switch_pm.write())
        
        if self.switch_webview is not None:
            b.write(self.switch_webview.write())
        
        b.write(Vector(self.results))
        
        b.write(Int(self.cache_time))
        
        b.write(Vector(self.users))
        
        return b.getvalue()