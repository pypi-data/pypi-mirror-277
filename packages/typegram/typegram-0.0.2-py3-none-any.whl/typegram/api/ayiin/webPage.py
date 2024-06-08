
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


WebPage = Union[api.types.WebPageEmpty, api.types.WebPagePending, api.types.WebPage, api.types.WebPageNotModified]


class WebPage(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            webPageEmpty
            webPagePending
            webPage
            webPageNotModified
    """

    QUALNAME = "typegram.api.ayiin.WebPage.WebPage"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/WebPage")