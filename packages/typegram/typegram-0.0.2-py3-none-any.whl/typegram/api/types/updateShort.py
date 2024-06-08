
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class UpdateShort(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Updates`.

    Details:
        - Layer: ``181``
        - ID: ``78D4DEC1``

update (:obj:`Update<typegram.api.ayiin.Update>`):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 11 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            account.getNotifyExceptions
            account.updateConnectedBot
            account.getBotBusinessConnection
            contacts.deleteContacts
            contacts.addContact
            contacts.acceptContact
            contacts.getLocated
            contacts.blockFromReplies
            messages.sendMessage
            messages.sendMedia
            messages.forwardMessages
            messages.editChatTitle
            messages.editChatPhoto
            messages.deleteChatUser
            messages.importChatInvite
            messages.startBot
            messages.migrateChat
            messages.sendInlineBotResult
            messages.editMessage
            messages.setGameScore
            messages.sendScreenshotNotification
            messages.sendMultiMedia
            messages.updatePinnedMessage
            messages.sendVote
            messages.getPollResults
            messages.editChatDefaultBannedRights
            messages.sendScheduledMessages
            messages.deleteScheduledMessages
            messages.setHistoryTTL
            messages.setChatTheme
            messages.hideChatJoinRequest
            messages.hideAllChatJoinRequests
            messages.toggleNoForwards
            messages.sendReaction
            messages.getMessagesReactions
            messages.setChatAvailableReactions
            messages.sendWebViewData
            messages.getExtendedMedia
            messages.sendBotRequestedPeer
            messages.setChatWallPaper
            messages.sendQuickReplyMessages
            messages.deleteQuickReplyMessages
            messages.editFactCheck
            messages.deleteFactCheck
            channels.createChannel
            channels.editAdmin
            channels.editTitle
            channels.editPhoto
            channels.joinChannel
            channels.leaveChannel
            channels.deleteChannel
            channels.toggleSignatures
            channels.editBanned
            channels.deleteHistory
            channels.togglePreHistoryHidden
            channels.editCreator
            channels.toggleSlowMode
            channels.convertToGigagroup
            channels.toggleJoinToSend
            channels.toggleJoinRequest
            channels.toggleForum
            channels.createForumTopic
            channels.editForumTopic
            channels.updatePinnedForumTopic
            channels.reorderPinnedForumTopics
            channels.toggleAntiSpam
            channels.toggleParticipantsHidden
            channels.updateColor
            channels.toggleViewForumAsMessages
            channels.updateEmojiStatus
            channels.setBoostsToUnblockRestrictions
            channels.restrictSponsoredMessages
            bots.allowSendMessage
            payments.assignAppStoreTransaction
            payments.assignPlayMarketTransaction
            payments.applyGiftCode
            payments.launchPrepaidGiveaway
            payments.refundStarsCharge
            phone.discardCall
            phone.setCallRating
            phone.createGroupCall
            phone.joinGroupCall
            phone.leaveGroupCall
            phone.inviteToGroupCall
            phone.discardGroupCall
            phone.toggleGroupCallSettings
            phone.toggleGroupCallRecord
            phone.editGroupCallParticipant
            phone.editGroupCallTitle
            phone.toggleGroupCallStartSubscription
            phone.startScheduledGroupCall
            phone.joinGroupCallPresentation
            phone.leaveGroupCallPresentation
            folders.editPeerFolders
            chatlists.joinChatlistInvite
            chatlists.joinChatlistUpdates
            chatlists.leaveChatlist
            stories.sendStory
            stories.editStory
            stories.activateStealthMode
            stories.sendReaction
    """

    __slots__: List[str] = ["update", "date"]

    ID = 0x78d4dec1
    QUALNAME = "types.updateShort"

    def __init__(self, *, update: "api.ayiin.Update", date: int) -> None:
        
                self.update = update  # Update
        
                self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateShort":
        # No flags
        
        update = Object.read(b)
        
        date = Int.read(b)
        
        return UpdateShort(update=update, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.update.write())
        
        b.write(Int(self.date))
        
        return b.getvalue()