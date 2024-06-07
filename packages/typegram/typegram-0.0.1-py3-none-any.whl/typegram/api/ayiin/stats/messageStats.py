
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


MessageStats = Union[api.types.stats.BroadcastStats, api.types.stats.MegagroupStats, api.types.stats.MessageStats, api.types.stats.StoryStats, api.types.stats.PublicForwards, api.types.stats.BroadcastRevenueStats, api.types.stats.BroadcastRevenueWithdrawalUrl, api.types.stats.BroadcastRevenueTransactions]


class MessageStats(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            stats.BroadcastStats
            stats.MegagroupStats
            stats.MessageStats
            stats.StoryStats
            stats.PublicForwards
            stats.BroadcastRevenueStats
            stats.BroadcastRevenueWithdrawalUrl
            stats.BroadcastRevenueTransactions
    """

    QUALNAME = "typegram.api.ayiin.messageStats.MessageStats"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/messageStats")