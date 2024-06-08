
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


Update = Union[api.types.UpdateNewMessage, api.types.UpdateMessageID, api.types.UpdateDeleteMessages, api.types.UpdateUserTyping, api.types.UpdateChatUserTyping, api.types.UpdateChatParticipants, api.types.UpdateUserStatus, api.types.UpdateUserName, api.types.UpdateNewAuthorization, api.types.UpdateNewEncryptedMessage, api.types.UpdateEncryptedChatTyping, api.types.UpdateEncryption, api.types.UpdateEncryptedMessagesRead, api.types.UpdateChatParticipantAdd, api.types.UpdateChatParticipantDelete, api.types.UpdateDcOptions, api.types.UpdateNotifySettings, api.types.UpdateServiceNotification, api.types.UpdatePrivacy, api.types.UpdateUserPhone, api.types.UpdateReadHistoryInbox, api.types.UpdateReadHistoryOutbox, api.types.UpdateWebPage, api.types.UpdateReadMessagesContents, api.types.UpdateChannelTooLong, api.types.UpdateChannel, api.types.UpdateNewChannelMessage, api.types.UpdateReadChannelInbox, api.types.UpdateDeleteChannelMessages, api.types.UpdateChannelMessageViews, api.types.UpdateChatParticipantAdmin, api.types.UpdateNewStickerSet, api.types.UpdateStickerSetsOrder, api.types.UpdateStickerSets, api.types.UpdateBotInlineQuery, api.types.UpdateBotInlineSend, api.types.UpdateEditChannelMessage, api.types.UpdateBotCallbackQuery, api.types.UpdateEditMessage, api.types.UpdateInlineBotCallbackQuery, api.types.UpdateReadChannelOutbox, api.types.UpdateDraftMessage, api.types.UpdateChannelWebPage, api.types.UpdateDialogPinned, api.types.UpdatePinnedDialogs, api.types.UpdateBotWebhookJSON, api.types.UpdateBotWebhookJSONQuery, api.types.UpdateBotShippingQuery, api.types.UpdateBotPrecheckoutQuery, api.types.UpdatePhoneCall, api.types.UpdateLangPackTooLong, api.types.UpdateLangPack, api.types.UpdateChannelReadMessagesContents, api.types.UpdateChannelAvailableMessages, api.types.UpdateDialogUnreadMark, api.types.UpdateMessagePoll, api.types.UpdateChatDefaultBannedRights, api.types.UpdateFolderPeers, api.types.UpdatePeerSettings, api.types.UpdatePeerLocated, api.types.UpdateNewScheduledMessage, api.types.UpdateDeleteScheduledMessages, api.types.UpdateTheme, api.types.UpdateGeoLiveViewed, api.types.UpdateMessagePollVote, api.types.UpdateDialogFilter, api.types.UpdateDialogFilterOrder, api.types.UpdatePhoneCallSignalingData, api.types.UpdateChannelMessageForwards, api.types.UpdateReadChannelDiscussionInbox, api.types.UpdateReadChannelDiscussionOutbox, api.types.UpdatePeerBlocked, api.types.UpdateChannelUserTyping, api.types.UpdatePinnedMessages, api.types.UpdatePinnedChannelMessages, api.types.UpdateChat, api.types.UpdateGroupCallParticipants, api.types.UpdateGroupCall, api.types.UpdatePeerHistoryTTL, api.types.UpdateChatParticipant, api.types.UpdateChannelParticipant, api.types.UpdateBotStopped, api.types.UpdateGroupCallConnection, api.types.UpdateBotCommands, api.types.UpdatePendingJoinRequests, api.types.UpdateBotChatInviteRequester, api.types.UpdateMessageReactions, api.types.UpdateWebViewResultSent, api.types.UpdateBotMenuButton, api.types.UpdateTranscribedAudio, api.types.UpdateUserEmojiStatus, api.types.UpdateMoveStickerSetToTop, api.types.UpdateMessageExtendedMedia, api.types.UpdateChannelPinnedTopic, api.types.UpdateChannelPinnedTopics, api.types.UpdateUser, api.types.UpdateStory, api.types.UpdateReadStories, api.types.UpdateStoryID, api.types.UpdateStoriesStealthMode, api.types.UpdateSentStoryReaction, api.types.UpdateBotChatBoost, api.types.UpdateChannelViewForumAsMessages, api.types.UpdatePeerWallpaper, api.types.UpdateBotMessageReaction, api.types.UpdateBotMessageReactions, api.types.UpdateSavedDialogPinned, api.types.UpdatePinnedSavedDialogs, api.types.UpdateSmsJob, api.types.UpdateQuickReplies, api.types.UpdateNewQuickReply, api.types.UpdateDeleteQuickReply, api.types.UpdateQuickReplyMessage, api.types.UpdateDeleteQuickReplyMessages, api.types.UpdateBotBusinessConnect, api.types.UpdateBotNewBusinessMessage, api.types.UpdateBotEditBusinessMessage, api.types.UpdateBotDeleteBusinessMessage, api.types.UpdateNewStoryReaction, api.types.UpdateBroadcastRevenueTransactions, api.types.UpdateStarsBalance]


class Update(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 121 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            updateNewMessage
            updateMessageID
            updateDeleteMessages
            updateUserTyping
            updateChatUserTyping
            updateChatParticipants
            updateUserStatus
            updateUserName
            updateNewAuthorization
            updateNewEncryptedMessage
            updateEncryptedChatTyping
            updateEncryption
            updateEncryptedMessagesRead
            updateChatParticipantAdd
            updateChatParticipantDelete
            updateDcOptions
            updateNotifySettings
            updateServiceNotification
            updatePrivacy
            updateUserPhone
            updateReadHistoryInbox
            updateReadHistoryOutbox
            updateWebPage
            updateReadMessagesContents
            updateChannelTooLong
            updateChannel
            updateNewChannelMessage
            updateReadChannelInbox
            updateDeleteChannelMessages
            updateChannelMessageViews
            updateChatParticipantAdmin
            updateNewStickerSet
            updateStickerSetsOrder
            updateStickerSets
            updateBotInlineQuery
            updateBotInlineSend
            updateEditChannelMessage
            updateBotCallbackQuery
            updateEditMessage
            updateInlineBotCallbackQuery
            updateReadChannelOutbox
            updateDraftMessage
            updateChannelWebPage
            updateDialogPinned
            updatePinnedDialogs
            updateBotWebhookJSON
            updateBotWebhookJSONQuery
            updateBotShippingQuery
            updateBotPrecheckoutQuery
            updatePhoneCall
            updateLangPackTooLong
            updateLangPack
            updateChannelReadMessagesContents
            updateChannelAvailableMessages
            updateDialogUnreadMark
            updateMessagePoll
            updateChatDefaultBannedRights
            updateFolderPeers
            updatePeerSettings
            updatePeerLocated
            updateNewScheduledMessage
            updateDeleteScheduledMessages
            updateTheme
            updateGeoLiveViewed
            updateMessagePollVote
            updateDialogFilter
            updateDialogFilterOrder
            updatePhoneCallSignalingData
            updateChannelMessageForwards
            updateReadChannelDiscussionInbox
            updateReadChannelDiscussionOutbox
            updatePeerBlocked
            updateChannelUserTyping
            updatePinnedMessages
            updatePinnedChannelMessages
            updateChat
            updateGroupCallParticipants
            updateGroupCall
            updatePeerHistoryTTL
            updateChatParticipant
            updateChannelParticipant
            updateBotStopped
            updateGroupCallConnection
            updateBotCommands
            updatePendingJoinRequests
            updateBotChatInviteRequester
            updateMessageReactions
            updateWebViewResultSent
            updateBotMenuButton
            updateTranscribedAudio
            updateUserEmojiStatus
            updateMoveStickerSetToTop
            updateMessageExtendedMedia
            updateChannelPinnedTopic
            updateChannelPinnedTopics
            updateUser
            updateStory
            updateReadStories
            updateStoryID
            updateStoriesStealthMode
            updateSentStoryReaction
            updateBotChatBoost
            updateChannelViewForumAsMessages
            updatePeerWallpaper
            updateBotMessageReaction
            updateBotMessageReactions
            updateSavedDialogPinned
            updatePinnedSavedDialogs
            updateSmsJob
            updateQuickReplies
            updateNewQuickReply
            updateDeleteQuickReply
            updateQuickReplyMessage
            updateDeleteQuickReplyMessages
            updateBotBusinessConnect
            updateBotNewBusinessMessage
            updateBotEditBusinessMessage
            updateBotDeleteBusinessMessage
            updateNewStoryReaction
            updateBroadcastRevenueTransactions
            updateStarsBalance
    """

    QUALNAME = "typegram.api.ayiin.Update.Update"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/Update")