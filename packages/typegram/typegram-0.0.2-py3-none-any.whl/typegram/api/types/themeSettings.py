
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class ThemeSettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ThemeSettings`.

    Details:
        - Layer: ``181``
        - ID: ``FA58B6D4``

base_theme (:obj:`BaseTheme<typegram.api.ayiin.BaseTheme>`):
                    N/A
                
        accent_color (``int`` ``32-bit``):
                    N/A
                
        message_colors_animated (``bool``, *optional*):
                    N/A
                
        outbox_accent_color (``int`` ``32-bit``, *optional*):
                    N/A
                
        message_colors (List of ``int`` ``32-bit``, *optional*):
                    N/A
                
        wallpaper (:obj:`WallPaper<typegram.api.ayiin.WallPaper>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["base_theme", "accent_color", "message_colors_animated", "outbox_accent_color", "message_colors", "wallpaper"]

    ID = 0xfa58b6d4
    QUALNAME = "types.themeSettings"

    def __init__(self, *, base_theme: "api.ayiin.BaseTheme", accent_color: int, message_colors_animated: Optional[bool] = None, outbox_accent_color: Optional[int] = None, message_colors: Optional[List[int]] = None, wallpaper: "api.ayiin.WallPaper" = None) -> None:
        
                self.base_theme = base_theme  # BaseTheme
        
                self.accent_color = accent_color  # int
        
                self.message_colors_animated = message_colors_animated  # true
        
                self.outbox_accent_color = outbox_accent_color  # int
        
                self.message_colors = message_colors  # int
        
                self.wallpaper = wallpaper  # WallPaper

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ThemeSettings":
        
        flags = Int.read(b)
        
        message_colors_animated = True if flags & (1 << 2) else False
        base_theme = Object.read(b)
        
        accent_color = Int.read(b)
        
        outbox_accent_color = Int.read(b) if flags & (1 << 3) else None
        message_colors = Object.read(b, Int) if flags & (1 << 0) else []
        
        wallpaper = Object.read(b) if flags & (1 << 1) else None
        
        return ThemeSettings(base_theme=base_theme, accent_color=accent_color, message_colors_animated=message_colors_animated, outbox_accent_color=outbox_accent_color, message_colors=message_colors, wallpaper=wallpaper)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.base_theme.write())
        
        b.write(Int(self.accent_color))
        
        if self.outbox_accent_color is not None:
            b.write(Int(self.outbox_accent_color))
        
        if self.message_colors is not None:
            b.write(Vector(self.message_colors, Int))
        
        if self.wallpaper is not None:
            b.write(self.wallpaper.write())
        
        return b.getvalue()