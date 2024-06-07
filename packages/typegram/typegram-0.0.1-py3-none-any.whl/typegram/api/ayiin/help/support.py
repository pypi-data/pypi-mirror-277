
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


Support = Union[api.types.help.AppUpdate, api.types.help.InviteText, api.types.help.Support, api.types.help.TermsOfService, api.types.help.RecentMeUrls, api.types.help.TermsOfServiceUpdate, api.types.help.DeepLinkInfo, api.types.help.PassportConfig, api.types.help.SupportName, api.types.help.UserInfo, api.types.help.PromoData, api.types.help.CountryCode, api.types.help.Country, api.types.help.CountriesList, api.types.help.PremiumPromo, api.types.help.AppConfig, api.types.help.PeerColorSet, api.types.help.PeerColorOption, api.types.help.PeerColors, api.types.help.TimezonesList]


class Support(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 20 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            help.AppUpdate
            help.InviteText
            help.Support
            help.TermsOfService
            help.RecentMeUrls
            help.TermsOfServiceUpdate
            help.DeepLinkInfo
            help.PassportConfig
            help.SupportName
            help.UserInfo
            help.PromoData
            help.CountryCode
            help.Country
            help.CountriesList
            help.PremiumPromo
            help.AppConfig
            help.PeerColorSet
            help.PeerColorOption
            help.PeerColors
            help.TimezonesList
    """

    QUALNAME = "typegram.api.ayiin.support.Support"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/support")