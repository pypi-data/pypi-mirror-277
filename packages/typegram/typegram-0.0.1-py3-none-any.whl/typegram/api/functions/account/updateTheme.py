
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



class UpdateTheme(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``2BF40CCC``

format (``str``):
                    N/A
                
        theme (:obj:`InputTheme<typegram.api.ayiin.InputTheme>`):
                    N/A
                
        slug (``str``, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        document (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`, *optional*):
                    N/A
                
        settings (List of :obj:`InputThemeSettings<typegram.api.ayiin.InputThemeSettings>`, *optional*):
                    N/A
                
    Returns:
        :obj:`Theme<typegram.api.ayiin.Theme>`
    """

    __slots__: List[str] = ["format", "theme", "slug", "title", "document", "settings"]

    ID = 0x2bf40ccc
    QUALNAME = "functions.functions.Theme"

    def __init__(self, *, format: str, theme: "ayiin.InputTheme", slug: Optional[str] = None, title: Optional[str] = None, document: "ayiin.InputDocument" = None, settings: Optional[List["ayiin.InputThemeSettings"]] = None) -> None:
        
                self.format = format  # string
        
                self.theme = theme  # InputTheme
        
                self.slug = slug  # string
        
                self.title = title  # string
        
                self.document = document  # InputDocument
        
                self.settings = settings  # InputThemeSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateTheme":
        
        flags = Int.read(b)
        
        format = String.read(b)
        
        theme = Object.read(b)
        
        slug = String.read(b) if flags & (1 << 0) else None
        title = String.read(b) if flags & (1 << 1) else None
        document = Object.read(b) if flags & (1 << 2) else None
        
        settings = Object.read(b) if flags & (1 << 3) else []
        
        return UpdateTheme(format=format, theme=theme, slug=slug, title=title, document=document, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.format))
        
        b.write(self.theme.write())
        
        if self.slug is not None:
            b.write(String(self.slug))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.settings is not None:
            b.write(Vector(self.settings))
        
        return b.getvalue()