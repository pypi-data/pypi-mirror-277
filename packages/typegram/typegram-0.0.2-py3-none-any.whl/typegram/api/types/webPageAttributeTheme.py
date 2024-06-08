
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



class WebPageAttributeTheme(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WebPageAttribute`.

    Details:
        - Layer: ``181``
        - ID: ``54B56617``

documents (List of :obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
        settings (:obj:`ThemeSettings<typegram.api.ayiin.ThemeSettings>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["documents", "settings"]

    ID = 0x54b56617
    QUALNAME = "types.webPageAttributeTheme"

    def __init__(self, *, documents: Optional[List["api.ayiin.Document"]] = None, settings: "api.ayiin.ThemeSettings" = None) -> None:
        
                self.documents = documents  # Document
        
                self.settings = settings  # ThemeSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeTheme":
        
        flags = Int.read(b)
        
        documents = Object.read(b) if flags & (1 << 0) else []
        
        settings = Object.read(b) if flags & (1 << 1) else None
        
        return WebPageAttributeTheme(documents=documents, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.documents is not None:
            b.write(Vector(self.documents))
        
        if self.settings is not None:
            b.write(self.settings.write())
        
        return b.getvalue()