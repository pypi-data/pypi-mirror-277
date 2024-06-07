
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



class TranscribedAudio(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.TranscribedAudio`.

    Details:
        - Layer: ``181``
        - ID: ``CFB9D957``

transcription_id (``int`` ``64-bit``):
                    N/A
                
        text (``str``):
                    N/A
                
        pending (``bool``, *optional*):
                    N/A
                
        trial_remains_num (``int`` ``32-bit``, *optional*):
                    N/A
                
        trial_remains_until_date (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 25 functions.

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

    __slots__: List[str] = ["transcription_id", "text", "pending", "trial_remains_num", "trial_remains_until_date"]

    ID = 0xcfb9d957
    QUALNAME = "functions.typesmessages.TranscribedAudio"

    def __init__(self, *, transcription_id: int, text: str, pending: Optional[bool] = None, trial_remains_num: Optional[int] = None, trial_remains_until_date: Optional[int] = None) -> None:
        
                self.transcription_id = transcription_id  # long
        
                self.text = text  # string
        
                self.pending = pending  # true
        
                self.trial_remains_num = trial_remains_num  # int
        
                self.trial_remains_until_date = trial_remains_until_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TranscribedAudio":
        
        flags = Int.read(b)
        
        pending = True if flags & (1 << 0) else False
        transcription_id = Long.read(b)
        
        text = String.read(b)
        
        trial_remains_num = Int.read(b) if flags & (1 << 1) else None
        trial_remains_until_date = Int.read(b) if flags & (1 << 1) else None
        return TranscribedAudio(transcription_id=transcription_id, text=text, pending=pending, trial_remains_num=trial_remains_num, trial_remains_until_date=trial_remains_until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.transcription_id))
        
        b.write(String(self.text))
        
        if self.trial_remains_num is not None:
            b.write(Int(self.trial_remains_num))
        
        if self.trial_remains_until_date is not None:
            b.write(Int(self.trial_remains_until_date))
        
        return b.getvalue()