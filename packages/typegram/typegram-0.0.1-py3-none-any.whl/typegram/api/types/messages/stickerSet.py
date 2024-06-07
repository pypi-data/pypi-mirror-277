
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



class StickerSet(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.StickerSet`.

    Details:
        - Layer: ``181``
        - ID: ``6E153F16``

set (:obj:`StickerSet<typegram.api.ayiin.StickerSet>`):
                    N/A
                
        packs (List of :obj:`StickerPack<typegram.api.ayiin.StickerPack>`):
                    N/A
                
        keywords (List of :obj:`StickerKeyword<typegram.api.ayiin.StickerKeyword>`):
                    N/A
                
        documents (List of :obj:`Document<typegram.api.ayiin.Document>`):
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

    __slots__: List[str] = ["set", "packs", "keywords", "documents"]

    ID = 0x6e153f16
    QUALNAME = "functions.typesmessages.StickerSet"

    def __init__(self, *, set: "ayiin.StickerSet", packs: List["ayiin.StickerPack"], keywords: List["ayiin.StickerKeyword"], documents: List["ayiin.Document"]) -> None:
        
                self.set = set  # StickerSet
        
                self.packs = packs  # StickerPack
        
                self.keywords = keywords  # StickerKeyword
        
                self.documents = documents  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSet":
        # No flags
        
        set = Object.read(b)
        
        packs = Object.read(b)
        
        keywords = Object.read(b)
        
        documents = Object.read(b)
        
        return StickerSet(set=set, packs=packs, keywords=keywords, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.set.write())
        
        b.write(Vector(self.packs))
        
        b.write(Vector(self.keywords))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()