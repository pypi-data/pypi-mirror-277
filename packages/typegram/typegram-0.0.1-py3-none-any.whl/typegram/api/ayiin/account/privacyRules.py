
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


PrivacyRules = Union[api.types.account.PrivacyRules, api.types.account.Authorizations, api.types.account.Password, api.types.account.PasswordSettings, api.types.account.PasswordInputSettings, api.types.account.TmpPassword, api.types.account.WebAuthorizations, api.types.account.AuthorizationForm, api.types.account.SentEmailCode, api.types.account.Takeout, api.types.account.WallPapers, api.types.account.AutoDownloadSettings, api.types.account.Themes, api.types.account.ContentSettings, api.types.account.ResetPasswordResult, api.types.account.SavedRingtones, api.types.account.SavedRingtone, api.types.account.EmojiStatuses, api.types.account.EmailVerified, api.types.account.AutoSaveSettings, api.types.account.ConnectedBots, api.types.account.BusinessChatLinks, api.types.account.ResolvedBusinessChatLinks]


class PrivacyRules(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 23 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            account.PrivacyRules
            account.Authorizations
            account.Password
            account.PasswordSettings
            account.PasswordInputSettings
            account.TmpPassword
            account.WebAuthorizations
            account.AuthorizationForm
            account.SentEmailCode
            account.Takeout
            account.WallPapers
            account.AutoDownloadSettings
            account.Themes
            account.ContentSettings
            account.ResetPasswordResult
            account.SavedRingtones
            account.SavedRingtone
            account.EmojiStatuses
            account.EmailVerified
            account.AutoSaveSettings
            account.ConnectedBots
            account.BusinessChatLinks
            account.ResolvedBusinessChatLinks
    """

    QUALNAME = "typegram.api.ayiin.privacyRules.PrivacyRules"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/privacyRules")