
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

from typing import Union, List, Optional

from typegram import api
from typegram.api.object import Object


AffectedMessages = Union[api.types.messages.Dialogs, api.types.messages.Messages, api.types.messages.Chats, api.types.messages.ChatFull, api.types.messages.AffectedHistory, api.types.messages.DhConfig, api.types.messages.SentEncryptedMessage, api.types.messages.Stickers, api.types.messages.AllStickers, api.types.messages.AffectedMessages, api.types.messages.StickerSet, api.types.messages.SavedGifs, api.types.messages.BotResults, api.types.messages.BotCallbackAnswer, api.types.messages.MessageEditData, api.types.messages.PeerDialogs, api.types.messages.FeaturedStickers, api.types.messages.RecentStickers, api.types.messages.ArchivedStickers, api.types.messages.StickerSetInstallResult, api.types.messages.HighScores, api.types.messages.FavedStickers, api.types.messages.FoundStickerSets, api.types.messages.SearchCounter, api.types.messages.InactiveChats, api.types.messages.VotesList, api.types.messages.MessageViews, api.types.messages.DiscussionMessage, api.types.messages.HistoryImport, api.types.messages.HistoryImportParsed, api.types.messages.AffectedFoundMessages, api.types.messages.ExportedChatInvites, api.types.messages.ExportedChatInvite, api.types.messages.ChatInviteImporters, api.types.messages.ChatAdminsWithInvites, api.types.messages.CheckedHistoryImportPeer, api.types.messages.SponsoredMessages, api.types.messages.SearchResultsCalendar, api.types.messages.SearchResultsPositions, api.types.messages.PeerSettings, api.types.messages.MessageReactionsList, api.types.messages.AvailableReactions, api.types.messages.TranscribedAudio, api.types.messages.Reactions, api.types.messages.ForumTopics, api.types.messages.EmojiGroups, api.types.messages.TranslatedText, api.types.messages.BotApp, api.types.messages.WebPage, api.types.messages.SavedDialogs, api.types.messages.SavedReactionTags, api.types.messages.QuickReplies, api.types.messages.DialogFilters, api.types.messages.MyStickers, api.types.messages.InvitedUsers, api.types.messages.AvailableEffects]


class AffectedMessages(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 56 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            messages.Dialogs
            messages.Messages
            messages.Chats
            messages.ChatFull
            messages.AffectedHistory
            messages.DhConfig
            messages.SentEncryptedMessage
            messages.Stickers
            messages.AllStickers
            messages.AffectedMessages
            messages.StickerSet
            messages.SavedGifs
            messages.BotResults
            messages.BotCallbackAnswer
            messages.MessageEditData
            messages.PeerDialogs
            messages.FeaturedStickers
            messages.RecentStickers
            messages.ArchivedStickers
            messages.StickerSetInstallResult
            messages.HighScores
            messages.FavedStickers
            messages.FoundStickerSets
            messages.SearchCounter
            messages.InactiveChats
            messages.VotesList
            messages.MessageViews
            messages.DiscussionMessage
            messages.HistoryImport
            messages.HistoryImportParsed
            messages.AffectedFoundMessages
            messages.ExportedChatInvites
            messages.ExportedChatInvite
            messages.ChatInviteImporters
            messages.ChatAdminsWithInvites
            messages.CheckedHistoryImportPeer
            messages.SponsoredMessages
            messages.SearchResultsCalendar
            messages.SearchResultsPositions
            messages.PeerSettings
            messages.MessageReactionsList
            messages.AvailableReactions
            messages.TranscribedAudio
            messages.Reactions
            messages.ForumTopics
            messages.EmojiGroups
            messages.TranslatedText
            messages.BotApp
            messages.WebPage
            messages.SavedDialogs
            messages.SavedReactionTags
            messages.QuickReplies
            messages.DialogFilters
            messages.MyStickers
            messages.InvitedUsers
            messages.AvailableEffects
    """

    QUALNAME = "typegram.api.ayiin.affectedMessages.AffectedMessages"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/affectedMessages")