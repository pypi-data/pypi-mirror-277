
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



class UpdateShortSentMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Updates`.

    Details:
        - Layer: ``181``
        - ID: ``9015E101``

id (``int`` ``32-bit``):
                    N/A
                
        pts (``int`` ``32-bit``):
                    N/A
                
        pts_count (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        out (``bool``, *optional*):
                    N/A
                
        media (:obj:`MessageMedia<typegram.api.ayiin.MessageMedia>`, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        ttl_period (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 22 functions.

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

    __slots__: List[str] = ["id", "pts", "pts_count", "date", "out", "media", "entities", "ttl_period"]

    ID = 0x9015e101
    QUALNAME = "types.updateShortSentMessage"

    def __init__(self, *, id: int, pts: int, pts_count: int, date: int, out: Optional[bool] = None, media: "api.ayiin.MessageMedia" = None, entities: Optional[List["api.ayiin.MessageEntity"]] = None, ttl_period: Optional[int] = None) -> None:
        
                self.id = id  # int
        
                self.pts = pts  # int
        
                self.pts_count = pts_count  # int
        
                self.date = date  # int
        
                self.out = out  # true
        
                self.media = media  # MessageMedia
        
                self.entities = entities  # MessageEntity
        
                self.ttl_period = ttl_period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateShortSentMessage":
        
        flags = Int.read(b)
        
        out = True if flags & (1 << 1) else False
        id = Int.read(b)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        date = Int.read(b)
        
        media = Object.read(b) if flags & (1 << 9) else None
        
        entities = Object.read(b) if flags & (1 << 7) else []
        
        ttl_period = Int.read(b) if flags & (1 << 25) else None
        return UpdateShortSentMessage(id=id, pts=pts, pts_count=pts_count, date=date, out=out, media=media, entities=entities, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        b.write(Int(self.date))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()