
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

from io import BytesIO
from typing import Any, Union, List, Optional

from typegram.api import ayiin, functions
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class SetReactionsNotifySettings(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``316CE548``

settings (:obj:`ReactionsNotifySettings<typegram.api.ayiin.ReactionsNotifySettings>`):
                    N/A
                
    Returns:
        :obj:`ReactionsNotifySettings<typegram.api.ayiin.ReactionsNotifySettings>`
    """

    __slots__: List[str] = ["settings"]

    ID = 0x316ce548
    QUALNAME = "functions.functions.ReactionsNotifySettings"

    def __init__(self, *, settings: "ayiin.ReactionsNotifySettings") -> None:
        
                self.settings = settings  # ReactionsNotifySettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetReactionsNotifySettings":
        # No flags
        
        settings = Object.read(b)
        
        return SetReactionsNotifySettings(settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.settings.write())
        
        return b.getvalue()