
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


JoinAsPeers = Union[api.types.phone.PhoneCall, api.types.phone.GroupCall, api.types.phone.GroupParticipants, api.types.phone.JoinAsPeers, api.types.phone.ExportedGroupCallInvite, api.types.phone.GroupCallStreamChannels, api.types.phone.GroupCallStreamRtmpUrl]


class JoinAsPeers(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            phone.PhoneCall
            phone.GroupCall
            phone.GroupParticipants
            phone.JoinAsPeers
            phone.ExportedGroupCallInvite
            phone.GroupCallStreamChannels
            phone.GroupCallStreamRtmpUrl
    """

    QUALNAME = "typegram.api.ayiin.joinAsPeers.JoinAsPeers"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/joinAsPeers")