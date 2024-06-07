
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



class SaveTheme(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F257106C``

theme (:obj:`InputTheme<typegram.api.ayiin.InputTheme>`):
                    N/A
                
        unsave (``bool``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["theme", "unsave"]

    ID = 0xf257106c
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, theme: "ayiin.InputTheme", unsave: bool) -> None:
        
                self.theme = theme  # InputTheme
        
                self.unsave = unsave  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveTheme":
        # No flags
        
        theme = Object.read(b)
        
        unsave = Bool.read(b)
        
        return SaveTheme(theme=theme, unsave=unsave)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.theme.write())
        
        b.write(Bool(self.unsave))
        
        return b.getvalue()