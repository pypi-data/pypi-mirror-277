
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


MessageAction = Union[api.types.MessageActionChatCreate, api.types.MessageActionChatEditTitle, api.types.MessageActionChatEditPhoto, api.types.MessageActionChatAddUser, api.types.MessageActionChatDeleteUser, api.types.MessageActionChatJoinedByLink, api.types.MessageActionChannelCreate, api.types.MessageActionChatMigrateTo, api.types.MessageActionChannelMigrateFrom, api.types.MessageActionGameScore, api.types.MessageActionPaymentSentMe, api.types.MessageActionPaymentSent, api.types.MessageActionPhoneCall, api.types.MessageActionCustomAction, api.types.MessageActionBotAllowed, api.types.MessageActionSecureValuesSentMe, api.types.MessageActionSecureValuesSent, api.types.MessageActionGeoProximityReached, api.types.MessageActionGroupCall, api.types.MessageActionInviteToGroupCall, api.types.MessageActionSetMessagesTTL, api.types.MessageActionGroupCallScheduled, api.types.MessageActionSetChatTheme, api.types.MessageActionWebViewDataSentMe, api.types.MessageActionWebViewDataSent, api.types.MessageActionGiftPremium, api.types.MessageActionTopicCreate, api.types.MessageActionTopicEdit, api.types.MessageActionSuggestProfilePhoto, api.types.MessageActionRequestedPeer, api.types.MessageActionSetChatWallPaper, api.types.MessageActionGiftCode, api.types.MessageActionGiveawayResults, api.types.MessageActionBoostApply, api.types.MessageActionRequestedPeerSentMe]


class MessageAction(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 35 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            messageActionChatCreate
            messageActionChatEditTitle
            messageActionChatEditPhoto
            messageActionChatAddUser
            messageActionChatDeleteUser
            messageActionChatJoinedByLink
            messageActionChannelCreate
            messageActionChatMigrateTo
            messageActionChannelMigrateFrom
            messageActionGameScore
            messageActionPaymentSentMe
            messageActionPaymentSent
            messageActionPhoneCall
            messageActionCustomAction
            messageActionBotAllowed
            messageActionSecureValuesSentMe
            messageActionSecureValuesSent
            messageActionGeoProximityReached
            messageActionGroupCall
            messageActionInviteToGroupCall
            messageActionSetMessagesTTL
            messageActionGroupCallScheduled
            messageActionSetChatTheme
            messageActionWebViewDataSentMe
            messageActionWebViewDataSent
            messageActionGiftPremium
            messageActionTopicCreate
            messageActionTopicEdit
            messageActionSuggestProfilePhoto
            messageActionRequestedPeer
            messageActionSetChatWallPaper
            messageActionGiftCode
            messageActionGiveawayResults
            messageActionBoostApply
            messageActionRequestedPeerSentMe
    """

    QUALNAME = "typegram.api.ayiin.MessageAction.MessageAction"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/MessageAction")