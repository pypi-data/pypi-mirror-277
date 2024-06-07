
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


SponsoredMessageReportResult = Union[api.types.channels.ChannelParticipants, api.types.channels.ChannelParticipant, api.types.channels.AdminLogResults, api.types.channels.SendAsPeers, api.types.channels.SponsoredMessageReportResult]


class SponsoredMessageReportResult(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            channels.ChannelParticipants
            channels.ChannelParticipant
            channels.AdminLogResults
            channels.SendAsPeers
            channels.SponsoredMessageReportResult
    """

    QUALNAME = "typegram.api.ayiin.sponsoredMessageReportResult.SponsoredMessageReportResult"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/sponsoredMessageReportResult")