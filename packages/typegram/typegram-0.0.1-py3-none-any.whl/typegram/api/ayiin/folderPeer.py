
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


FolderPeer = Union[api.types.InputPeer, api.types.InputUser, api.types.InputContact, api.types.InputFile, api.types.InputMedia, api.types.InputChatPhoto, api.types.InputGeoPoint, api.types.InputPhoto, api.types.InputFileLocation, api.types.Peer, api.types.RpcResult, api.types.RpcError, api.types.RpcDropAnswer, api.types.User, api.types.UserProfilePhoto, api.types.UserStatus, api.types.Chat, api.types.ChatFull, api.types.ChatParticipant, api.types.ChatParticipants, api.types.ChatPhoto, api.types.Message, api.types.MessageMedia, api.types.MessageAction, api.types.Dialog, api.types.Photo, api.types.PhotoSize, api.types.GeoPoint, api.types.InputNotifyPeer, api.types.InputPeerNotifySettings, api.types.PeerNotifySettings, api.types.PeerSettings, api.types.WallPaper, api.types.UserFull, api.types.Contact, api.types.ImportedContact, api.types.ContactStatus, api.types.MessagesFilter, api.types.Update, api.types.Updates, api.types.DcOption, api.types.Config, api.types.NearestDc, api.types.EncryptedChat, api.types.InputEncryptedChat, api.types.EncryptedFile, api.types.InputEncryptedFile, api.types.EncryptedMessage, api.types.InputDocument, api.types.Document, api.types.NotifyPeer, api.types.SendMessageAction, api.types.InputPrivacyRule, api.types.PrivacyRule, api.types.AccountDaysTTL, api.types.DocumentAttribute, api.types.StickerPack, api.types.WebPage, api.types.Authorization, api.types.ReceivedNotifyMessage, api.types.ExportedChatInvite, api.types.ChatInvite, api.types.InputStickerSet, api.types.StickerSet, api.types.BotCommand, api.types.BotInfo, api.types.KeyboardButton, api.types.KeyboardButtonRow, api.types.ReplyMarkup, api.types.MessageEntity, api.types.InputChannel, api.types.MessageRange, api.types.ChannelMessagesFilter, api.types.ChannelParticipant, api.types.ChannelParticipantsFilter, api.types.InputBotInlineMessage, api.types.InputBotInlineResult, api.types.BotInlineMessage, api.types.BotInlineResult, api.types.ExportedMessageLink, api.types.MessageFwdHeader, api.types.InputBotInlineMessageID, api.types.InlineBotSwitchPM, api.types.TopPeer, api.types.TopPeerCategoryPeers, api.types.DraftMessage, api.types.StickerSetCovered, api.types.MaskCoords, api.types.InputStickeredMedia, api.types.Game, api.types.InputGame, api.types.HighScore, api.types.RichText, api.types.PageBlock, api.types.DataJSON, api.types.LabeledPrice, api.types.Invoice, api.types.PaymentCharge, api.types.PostAddress, api.types.PaymentRequestedInfo, api.types.PaymentSavedCredentials, api.types.WebDocument, api.types.InputWebDocument, api.types.InputWebFileLocation, api.types.InputPaymentCredentials, api.types.ShippingOption, api.types.InputStickerSetItem, api.types.InputPhoneCall, api.types.PhoneCall, api.types.PhoneConnection, api.types.PhoneCallProtocol, api.types.CdnPublicKey, api.types.CdnConfig, api.types.LangPackString, api.types.LangPackDifference, api.types.LangPackLanguage, api.types.ChannelAdminLogEventAction, api.types.ChannelAdminLogEvent, api.types.ChannelAdminLogEventsFilter, api.types.PopularContact, api.types.RecentMeUrl, api.types.InputSingleMedia, api.types.WebAuthorization, api.types.InputMessage, api.types.InputDialogPeer, api.types.DialogPeer, api.types.FileHash, api.types.InputClientProxy, api.types.InputSecureFile, api.types.SecureFile, api.types.SecureData, api.types.SecurePlainData, api.types.SecureValue, api.types.InputSecureValue, api.types.SecureValueHash, api.types.SecureValueError, api.types.SecureCredentialsEncrypted, api.types.SavedContact, api.types.PasswordKdfAlgo, api.types.SecurePasswordKdfAlgo, api.types.SecureSecretSettings, api.types.InputCheckPasswordSRP, api.types.SecureRequiredType, api.types.InputAppEvent, api.types.JSONObjectValue, api.types.JSONValue, api.types.PageTableCell, api.types.PageTableRow, api.types.PageCaption, api.types.PageListItem, api.types.PageListOrderedItem, api.types.PageRelatedArticle, api.types.Page, api.types.PollAnswer, api.types.Poll, api.types.PollAnswerVoters, api.types.PollResults, api.types.ChatOnlines, api.types.StatsURL, api.types.ChatAdminRights, api.types.ChatBannedRights, api.types.InputWallPaper, api.types.CodeSettings, api.types.WallPaperSettings, api.types.AutoDownloadSettings, api.types.EmojiKeyword, api.types.EmojiKeywordsDifference, api.types.EmojiURL, api.types.EmojiLanguage, api.types.Folder, api.types.InputFolderPeer, api.types.FolderPeer, api.types.UrlAuthResult, api.types.ChannelLocation, api.types.PeerLocated, api.types.RestrictionReason, api.types.InputTheme, api.types.Theme, api.types.InputThemeSettings, api.types.ThemeSettings, api.types.WebPageAttribute, api.types.BankCardOpenUrl, api.types.DialogFilter, api.types.DialogFilterSuggested, api.types.StatsDateRangeDays, api.types.StatsAbsValueAndPrev, api.types.StatsPercentValue, api.types.StatsGraph, api.types.VideoSize, api.types.StatsGroupTopPoster, api.types.StatsGroupTopAdmin, api.types.StatsGroupTopInviter, api.types.GlobalPrivacySettings, api.types.MessageViews, api.types.MessageReplyHeader, api.types.MessageReplies, api.types.PeerBlocked, api.types.GroupCall, api.types.InputGroupCall, api.types.GroupCallParticipant, api.types.ChatInviteImporter, api.types.ChatAdminWithInvites, api.types.GroupCallParticipantVideoSourceGroup, api.types.GroupCallParticipantVideo, api.types.BotCommandScope, api.types.SponsoredMessage, api.types.SearchResultsCalendarPeriod, api.types.SearchResultsPosition, api.types.ReactionCount, api.types.MessageReactions, api.types.AvailableReaction, api.types.MessagePeerReaction, api.types.GroupCallStreamChannel, api.types.AttachMenuBotIconColor, api.types.AttachMenuBotIcon, api.types.AttachMenuBot, api.types.AttachMenuBots, api.types.AttachMenuBotsBot, api.types.WebViewResult, api.types.SimpleWebViewResult, api.types.WebViewMessageSent, api.types.BotMenuButton, api.types.NotificationSound, api.types.InputInvoice, api.types.InputStorePaymentPurpose, api.types.PremiumGiftOption, api.types.PaymentFormMethod, api.types.EmojiStatus, api.types.Reaction, api.types.ChatReactions, api.types.EmailVerifyPurpose, api.types.EmailVerification, api.types.PremiumSubscriptionOption, api.types.SendAsPeer, api.types.MessageExtendedMedia, api.types.StickerKeyword, api.types.Username, api.types.ForumTopic, api.types.DefaultHistoryTTL, api.types.ExportedContactToken, api.types.RequestPeerType, api.types.EmojiList, api.types.EmojiGroup, api.types.TextWithEntities, api.types.AutoSaveSettings, api.types.AutoSaveException, api.types.InputBotApp, api.types.BotApp, api.types.AppWebViewResult, api.types.InlineBotWebView, api.types.ReadParticipantDate, api.types.InputChatlist, api.types.ExportedChatlistInvite, api.types.MessagePeerVote, api.types.StoryViews, api.types.StoryItem, api.types.StoryView, api.types.InputReplyTo, api.types.ExportedStoryLink, api.types.StoriesStealthMode, api.types.MediaAreaCoordinates, api.types.MediaArea, api.types.PeerStories, api.types.PremiumGiftCodeOption, api.types.PrepaidGiveaway, api.types.Boost, api.types.MyBoost, api.types.StoryFwdHeader, api.types.PostInteractionCounters, api.types.PublicForward, api.types.PeerColor, api.types.StoryReaction, api.types.SavedDialog, api.types.SavedReactionTag, api.types.OutboxReadDate, api.types.SmsJob, api.types.BusinessWeeklyOpen, api.types.BusinessWorkHours, api.types.BusinessLocation, api.types.InputBusinessRecipients, api.types.BusinessRecipients, api.types.BusinessAwayMessageSchedule, api.types.InputBusinessGreetingMessage, api.types.BusinessGreetingMessage, api.types.InputBusinessAwayMessage, api.types.BusinessAwayMessage, api.types.Timezone, api.types.QuickReply, api.types.InputQuickReplyShortcut, api.types.ConnectedBot, api.types.Birthday, api.types.BotBusinessConnection, api.types.InputBusinessIntro, api.types.BusinessIntro, api.types.InputCollectible, api.types.InputBusinessBotRecipients, api.types.BusinessBotRecipients, api.types.ContactBirthday, api.types.MissingInvitee, api.types.InputBusinessChatLink, api.types.BusinessChatLink, api.types.RequestedPeer, api.types.SponsoredMessageReportOption, api.types.BroadcastRevenueTransaction, api.types.ReactionsNotifySettings, api.types.BroadcastRevenueBalances, api.types.AvailableEffect, api.types.FactCheck, api.types.StarsTransactionPeer, api.types.StarsTopupOption, api.types.StarsTransaction]


class FolderPeer(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 311 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            .InputPeer
            .InputUser
            .InputContact
            .InputFile
            .InputMedia
            .InputChatPhoto
            .InputGeoPoint
            .InputPhoto
            .InputFileLocation
            .Peer
            .RpcResult
            .RpcError
            .RpcDropAnswer
            .User
            .UserProfilePhoto
            .UserStatus
            .Chat
            .ChatFull
            .ChatParticipant
            .ChatParticipants
            .ChatPhoto
            .Message
            .MessageMedia
            .MessageAction
            .Dialog
            .Photo
            .PhotoSize
            .GeoPoint
            .InputNotifyPeer
            .InputPeerNotifySettings
            .PeerNotifySettings
            .PeerSettings
            .WallPaper
            .UserFull
            .Contact
            .ImportedContact
            .ContactStatus
            .MessagesFilter
            .Update
            .Updates
            .DcOption
            .Config
            .NearestDc
            .EncryptedChat
            .InputEncryptedChat
            .EncryptedFile
            .InputEncryptedFile
            .EncryptedMessage
            .InputDocument
            .Document
            .NotifyPeer
            .SendMessageAction
            .InputPrivacyRule
            .PrivacyRule
            .AccountDaysTTL
            .DocumentAttribute
            .StickerPack
            .WebPage
            .Authorization
            .ReceivedNotifyMessage
            .ExportedChatInvite
            .ChatInvite
            .InputStickerSet
            .StickerSet
            .BotCommand
            .BotInfo
            .KeyboardButton
            .KeyboardButtonRow
            .ReplyMarkup
            .MessageEntity
            .InputChannel
            .MessageRange
            .ChannelMessagesFilter
            .ChannelParticipant
            .ChannelParticipantsFilter
            .InputBotInlineMessage
            .InputBotInlineResult
            .BotInlineMessage
            .BotInlineResult
            .ExportedMessageLink
            .MessageFwdHeader
            .InputBotInlineMessageID
            .InlineBotSwitchPM
            .TopPeer
            .TopPeerCategoryPeers
            .DraftMessage
            .StickerSetCovered
            .MaskCoords
            .InputStickeredMedia
            .Game
            .InputGame
            .HighScore
            .RichText
            .PageBlock
            .DataJSON
            .LabeledPrice
            .Invoice
            .PaymentCharge
            .PostAddress
            .PaymentRequestedInfo
            .PaymentSavedCredentials
            .WebDocument
            .InputWebDocument
            .InputWebFileLocation
            .InputPaymentCredentials
            .ShippingOption
            .InputStickerSetItem
            .InputPhoneCall
            .PhoneCall
            .PhoneConnection
            .PhoneCallProtocol
            .CdnPublicKey
            .CdnConfig
            .LangPackString
            .LangPackDifference
            .LangPackLanguage
            .ChannelAdminLogEventAction
            .ChannelAdminLogEvent
            .ChannelAdminLogEventsFilter
            .PopularContact
            .RecentMeUrl
            .InputSingleMedia
            .WebAuthorization
            .InputMessage
            .InputDialogPeer
            .DialogPeer
            .FileHash
            .InputClientProxy
            .InputSecureFile
            .SecureFile
            .SecureData
            .SecurePlainData
            .SecureValue
            .InputSecureValue
            .SecureValueHash
            .SecureValueError
            .SecureCredentialsEncrypted
            .SavedContact
            .PasswordKdfAlgo
            .SecurePasswordKdfAlgo
            .SecureSecretSettings
            .InputCheckPasswordSRP
            .SecureRequiredType
            .InputAppEvent
            .JSONObjectValue
            .JSONValue
            .PageTableCell
            .PageTableRow
            .PageCaption
            .PageListItem
            .PageListOrderedItem
            .PageRelatedArticle
            .Page
            .PollAnswer
            .Poll
            .PollAnswerVoters
            .PollResults
            .ChatOnlines
            .StatsURL
            .ChatAdminRights
            .ChatBannedRights
            .InputWallPaper
            .CodeSettings
            .WallPaperSettings
            .AutoDownloadSettings
            .EmojiKeyword
            .EmojiKeywordsDifference
            .EmojiURL
            .EmojiLanguage
            .Folder
            .InputFolderPeer
            .FolderPeer
            .UrlAuthResult
            .ChannelLocation
            .PeerLocated
            .RestrictionReason
            .InputTheme
            .Theme
            .InputThemeSettings
            .ThemeSettings
            .WebPageAttribute
            .BankCardOpenUrl
            .DialogFilter
            .DialogFilterSuggested
            .StatsDateRangeDays
            .StatsAbsValueAndPrev
            .StatsPercentValue
            .StatsGraph
            .VideoSize
            .StatsGroupTopPoster
            .StatsGroupTopAdmin
            .StatsGroupTopInviter
            .GlobalPrivacySettings
            .MessageViews
            .MessageReplyHeader
            .MessageReplies
            .PeerBlocked
            .GroupCall
            .InputGroupCall
            .GroupCallParticipant
            .ChatInviteImporter
            .ChatAdminWithInvites
            .GroupCallParticipantVideoSourceGroup
            .GroupCallParticipantVideo
            .BotCommandScope
            .SponsoredMessage
            .SearchResultsCalendarPeriod
            .SearchResultsPosition
            .ReactionCount
            .MessageReactions
            .AvailableReaction
            .MessagePeerReaction
            .GroupCallStreamChannel
            .AttachMenuBotIconColor
            .AttachMenuBotIcon
            .AttachMenuBot
            .AttachMenuBots
            .AttachMenuBotsBot
            .WebViewResult
            .SimpleWebViewResult
            .WebViewMessageSent
            .BotMenuButton
            .NotificationSound
            .InputInvoice
            .InputStorePaymentPurpose
            .PremiumGiftOption
            .PaymentFormMethod
            .EmojiStatus
            .Reaction
            .ChatReactions
            .EmailVerifyPurpose
            .EmailVerification
            .PremiumSubscriptionOption
            .SendAsPeer
            .MessageExtendedMedia
            .StickerKeyword
            .Username
            .ForumTopic
            .DefaultHistoryTTL
            .ExportedContactToken
            .RequestPeerType
            .EmojiList
            .EmojiGroup
            .TextWithEntities
            .AutoSaveSettings
            .AutoSaveException
            .InputBotApp
            .BotApp
            .AppWebViewResult
            .InlineBotWebView
            .ReadParticipantDate
            .InputChatlist
            .ExportedChatlistInvite
            .MessagePeerVote
            .StoryViews
            .StoryItem
            .StoryView
            .InputReplyTo
            .ExportedStoryLink
            .StoriesStealthMode
            .MediaAreaCoordinates
            .MediaArea
            .PeerStories
            .PremiumGiftCodeOption
            .PrepaidGiveaway
            .Boost
            .MyBoost
            .StoryFwdHeader
            .PostInteractionCounters
            .PublicForward
            .PeerColor
            .StoryReaction
            .SavedDialog
            .SavedReactionTag
            .OutboxReadDate
            .SmsJob
            .BusinessWeeklyOpen
            .BusinessWorkHours
            .BusinessLocation
            .InputBusinessRecipients
            .BusinessRecipients
            .BusinessAwayMessageSchedule
            .InputBusinessGreetingMessage
            .BusinessGreetingMessage
            .InputBusinessAwayMessage
            .BusinessAwayMessage
            .Timezone
            .QuickReply
            .InputQuickReplyShortcut
            .ConnectedBot
            .Birthday
            .BotBusinessConnection
            .InputBusinessIntro
            .BusinessIntro
            .InputCollectible
            .InputBusinessBotRecipients
            .BusinessBotRecipients
            .ContactBirthday
            .MissingInvitee
            .InputBusinessChatLink
            .BusinessChatLink
            .RequestedPeer
            .SponsoredMessageReportOption
            .BroadcastRevenueTransaction
            .ReactionsNotifySettings
            .BroadcastRevenueBalances
            .AvailableEffect
            .FactCheck
            .StarsTransactionPeer
            .StarsTopupOption
            .StarsTransaction
    """

    QUALNAME = "typegram.api.ayiin.folderPeer.FolderPeer"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/folderPeer")