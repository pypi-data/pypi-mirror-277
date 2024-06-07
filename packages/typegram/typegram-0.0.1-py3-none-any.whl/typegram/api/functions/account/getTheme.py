
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



class GetTheme(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3A5869EC``

format (``str``):
                    N/A
                
        theme (:obj:`InputTheme<typegram.api.ayiin.InputTheme>`):
                    N/A
                
    Returns:
        :obj:`Theme<typegram.api.ayiin.Theme>`
    """

    __slots__: List[str] = ["format", "theme"]

    ID = 0x3a5869ec
    QUALNAME = "functions.functions.Theme"

    def __init__(self, *, format: str, theme: "ayiin.InputTheme") -> None:
        
                self.format = format  # string
        
                self.theme = theme  # InputTheme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTheme":
        # No flags
        
        format = String.read(b)
        
        theme = Object.read(b)
        
        return GetTheme(format=format, theme=theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.format))
        
        b.write(self.theme.write())
        
        return b.getvalue()