
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


LoggedOut = Union[api.types.auth.SentCode, api.types.auth.Authorization, api.types.auth.ExportedAuthorization, api.types.auth.PasswordRecovery, api.types.auth.SentCodeType, api.types.auth.LoginToken, api.types.auth.LoggedOut]


class LoggedOut(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            auth.SentCode
            auth.Authorization
            auth.ExportedAuthorization
            auth.PasswordRecovery
            auth.SentCodeType
            auth.LoginToken
            auth.LoggedOut
    """

    QUALNAME = "typegram.api.ayiin.loggedOut.LoggedOut"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/loggedOut")