
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


RichText = Union[api.types.TextPlain, api.types.TextBold, api.types.TextItalic, api.types.TextUnderline, api.types.TextStrike, api.types.TextFixed, api.types.TextUrl, api.types.TextEmail, api.types.TextConcat, api.types.TextSubscript, api.types.TextSuperscript, api.types.TextMarked, api.types.TextPhone, api.types.TextImage, api.types.TextAnchor]


class RichText(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 15 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            textPlain
            textBold
            textItalic
            textUnderline
            textStrike
            textFixed
            textUrl
            textEmail
            textConcat
            textSubscript
            textSuperscript
            textMarked
            textPhone
            textImage
            textAnchor
    """

    QUALNAME = "typegram.api.ayiin.RichText.RichText"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/RichText")