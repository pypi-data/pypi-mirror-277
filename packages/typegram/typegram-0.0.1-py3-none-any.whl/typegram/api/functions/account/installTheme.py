
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



class InstallTheme(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``C727BB3B``

dark (``bool``, *optional*):
                    N/A
                
        theme (:obj:`InputTheme<typegram.api.ayiin.InputTheme>`, *optional*):
                    N/A
                
        format (``str``, *optional*):
                    N/A
                
        base_theme (:obj:`BaseTheme<typegram.api.ayiin.BaseTheme>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["dark", "theme", "format", "base_theme"]

    ID = 0xc727bb3b
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, dark: Optional[bool] = None, theme: "ayiin.InputTheme" = None, format: Optional[str] = None, base_theme: "ayiin.BaseTheme" = None) -> None:
        
                self.dark = dark  # true
        
                self.theme = theme  # InputTheme
        
                self.format = format  # string
        
                self.base_theme = base_theme  # BaseTheme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InstallTheme":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        theme = Object.read(b) if flags & (1 << 1) else None
        
        format = String.read(b) if flags & (1 << 2) else None
        base_theme = Object.read(b) if flags & (1 << 3) else None
        
        return InstallTheme(dark=dark, theme=theme, format=format, base_theme=base_theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.theme is not None:
            b.write(self.theme.write())
        
        if self.format is not None:
            b.write(String(self.format))
        
        if self.base_theme is not None:
            b.write(self.base_theme.write())
        
        return b.getvalue()