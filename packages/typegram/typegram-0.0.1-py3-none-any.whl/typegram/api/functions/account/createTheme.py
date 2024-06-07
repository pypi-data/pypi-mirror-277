
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



class CreateTheme(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``652E4400``

slug (``str``):
                    N/A
                
        title (``str``):
                    N/A
                
        document (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`, *optional*):
                    N/A
                
        settings (List of :obj:`InputThemeSettings<typegram.api.ayiin.InputThemeSettings>`, *optional*):
                    N/A
                
    Returns:
        :obj:`Theme<typegram.api.ayiin.Theme>`
    """

    __slots__: List[str] = ["slug", "title", "document", "settings"]

    ID = 0x652e4400
    QUALNAME = "functions.functions.Theme"

    def __init__(self, *, slug: str, title: str, document: "ayiin.InputDocument" = None, settings: Optional[List["ayiin.InputThemeSettings"]] = None) -> None:
        
                self.slug = slug  # string
        
                self.title = title  # string
        
                self.document = document  # InputDocument
        
                self.settings = settings  # InputThemeSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateTheme":
        
        flags = Int.read(b)
        
        slug = String.read(b)
        
        title = String.read(b)
        
        document = Object.read(b) if flags & (1 << 2) else None
        
        settings = Object.read(b) if flags & (1 << 3) else []
        
        return CreateTheme(slug=slug, title=title, document=document, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.slug))
        
        b.write(String(self.title))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.settings is not None:
            b.write(Vector(self.settings))
        
        return b.getvalue()