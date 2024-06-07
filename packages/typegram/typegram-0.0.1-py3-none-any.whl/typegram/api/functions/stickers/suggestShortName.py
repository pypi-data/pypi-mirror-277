
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



class SuggestShortName(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``4DAFC503``

title (``str``):
                    N/A
                
    Returns:
        :obj:`stickers.SuggestedShortName<typegram.api.ayiin.stickers.SuggestedShortName>`
    """

    __slots__: List[str] = ["title"]

    ID = 0x4dafc503
    QUALNAME = "functions.functionsstickers.SuggestedShortName"

    def __init__(self, *, title: str) -> None:
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SuggestShortName":
        # No flags
        
        title = String.read(b)
        
        return SuggestShortName(title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.title))
        
        return b.getvalue()