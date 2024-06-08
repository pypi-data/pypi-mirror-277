
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


StoryItem = Union[api.types.StoryItemDeleted, api.types.StoryItemSkipped, api.types.StoryItem]


class StoryItem(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            storyItemDeleted
            storyItemSkipped
            storyItem
    """

    QUALNAME = "typegram.api.ayiin.StoryItem.StoryItem"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/StoryItem")