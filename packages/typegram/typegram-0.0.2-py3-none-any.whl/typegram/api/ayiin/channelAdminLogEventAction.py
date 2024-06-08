
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


ChannelAdminLogEventAction = Union[api.types.ChannelAdminLogEventActionChangeTitle, api.types.ChannelAdminLogEventActionChangeAbout, api.types.ChannelAdminLogEventActionChangeUsername, api.types.ChannelAdminLogEventActionChangePhoto, api.types.ChannelAdminLogEventActionToggleInvites, api.types.ChannelAdminLogEventActionToggleSignatures, api.types.ChannelAdminLogEventActionUpdatePinned, api.types.ChannelAdminLogEventActionEditMessage, api.types.ChannelAdminLogEventActionDeleteMessage, api.types.ChannelAdminLogEventActionParticipantInvite, api.types.ChannelAdminLogEventActionParticipantToggleBan, api.types.ChannelAdminLogEventActionParticipantToggleAdmin, api.types.ChannelAdminLogEventActionChangeStickerSet, api.types.ChannelAdminLogEventActionTogglePreHistoryHidden, api.types.ChannelAdminLogEventActionDefaultBannedRights, api.types.ChannelAdminLogEventActionStopPoll, api.types.ChannelAdminLogEventActionChangeLinkedChat, api.types.ChannelAdminLogEventActionChangeLocation, api.types.ChannelAdminLogEventActionToggleSlowMode, api.types.ChannelAdminLogEventActionStartGroupCall, api.types.ChannelAdminLogEventActionDiscardGroupCall, api.types.ChannelAdminLogEventActionParticipantMute, api.types.ChannelAdminLogEventActionParticipantUnmute, api.types.ChannelAdminLogEventActionToggleGroupCallSetting, api.types.ChannelAdminLogEventActionParticipantJoinByInvite, api.types.ChannelAdminLogEventActionExportedInviteDelete, api.types.ChannelAdminLogEventActionExportedInviteRevoke, api.types.ChannelAdminLogEventActionExportedInviteEdit, api.types.ChannelAdminLogEventActionParticipantVolume, api.types.ChannelAdminLogEventActionChangeHistoryTTL, api.types.ChannelAdminLogEventActionParticipantJoinByRequest, api.types.ChannelAdminLogEventActionToggleNoForwards, api.types.ChannelAdminLogEventActionSendMessage, api.types.ChannelAdminLogEventActionChangeAvailableReactions, api.types.ChannelAdminLogEventActionChangeUsernames, api.types.ChannelAdminLogEventActionToggleForum, api.types.ChannelAdminLogEventActionCreateTopic, api.types.ChannelAdminLogEventActionEditTopic, api.types.ChannelAdminLogEventActionDeleteTopic, api.types.ChannelAdminLogEventActionPinTopic, api.types.ChannelAdminLogEventActionToggleAntiSpam, api.types.ChannelAdminLogEventActionChangePeerColor, api.types.ChannelAdminLogEventActionChangeProfilePeerColor, api.types.ChannelAdminLogEventActionChangeWallpaper, api.types.ChannelAdminLogEventActionChangeEmojiStatus, api.types.ChannelAdminLogEventActionChangeEmojiStickerSet]


class ChannelAdminLogEventAction(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 46 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            channelAdminLogEventActionChangeTitle
            channelAdminLogEventActionChangeAbout
            channelAdminLogEventActionChangeUsername
            channelAdminLogEventActionChangePhoto
            channelAdminLogEventActionToggleInvites
            channelAdminLogEventActionToggleSignatures
            channelAdminLogEventActionUpdatePinned
            channelAdminLogEventActionEditMessage
            channelAdminLogEventActionDeleteMessage
            channelAdminLogEventActionParticipantInvite
            channelAdminLogEventActionParticipantToggleBan
            channelAdminLogEventActionParticipantToggleAdmin
            channelAdminLogEventActionChangeStickerSet
            channelAdminLogEventActionTogglePreHistoryHidden
            channelAdminLogEventActionDefaultBannedRights
            channelAdminLogEventActionStopPoll
            channelAdminLogEventActionChangeLinkedChat
            channelAdminLogEventActionChangeLocation
            channelAdminLogEventActionToggleSlowMode
            channelAdminLogEventActionStartGroupCall
            channelAdminLogEventActionDiscardGroupCall
            channelAdminLogEventActionParticipantMute
            channelAdminLogEventActionParticipantUnmute
            channelAdminLogEventActionToggleGroupCallSetting
            channelAdminLogEventActionParticipantJoinByInvite
            channelAdminLogEventActionExportedInviteDelete
            channelAdminLogEventActionExportedInviteRevoke
            channelAdminLogEventActionExportedInviteEdit
            channelAdminLogEventActionParticipantVolume
            channelAdminLogEventActionChangeHistoryTTL
            channelAdminLogEventActionParticipantJoinByRequest
            channelAdminLogEventActionToggleNoForwards
            channelAdminLogEventActionSendMessage
            channelAdminLogEventActionChangeAvailableReactions
            channelAdminLogEventActionChangeUsernames
            channelAdminLogEventActionToggleForum
            channelAdminLogEventActionCreateTopic
            channelAdminLogEventActionEditTopic
            channelAdminLogEventActionDeleteTopic
            channelAdminLogEventActionPinTopic
            channelAdminLogEventActionToggleAntiSpam
            channelAdminLogEventActionChangePeerColor
            channelAdminLogEventActionChangeProfilePeerColor
            channelAdminLogEventActionChangeWallpaper
            channelAdminLogEventActionChangeEmojiStatus
            channelAdminLogEventActionChangeEmojiStickerSet
    """

    QUALNAME = "typegram.api.ayiin.ChannelAdminLogEventAction.ChannelAdminLogEventAction"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/ChannelAdminLogEventAction")