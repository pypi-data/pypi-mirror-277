
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



class Theme(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Theme`.

    Details:
        - Layer: ``181``
        - ID: ``A00E67D6``

id (``int`` ``64-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        slug (``str``):
                    N/A
                
        title (``str``):
                    N/A
                
        creator (``bool``, *optional*):
                    N/A
                
        default (``bool``, *optional*):
                    N/A
                
        for_chat (``bool``, *optional*):
                    N/A
                
        document (:obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
        settings (List of :obj:`ThemeSettings<typegram.api.ayiin.ThemeSettings>`, *optional*):
                    N/A
                
        emoticon (``str``, *optional*):
                    N/A
                
        installs_count (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 5 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            account.createTheme
            account.updateTheme
            account.getTheme
    """

    __slots__: List[str] = ["id", "access_hash", "slug", "title", "creator", "default", "for_chat", "document", "settings", "emoticon", "installs_count"]

    ID = 0xa00e67d6
    QUALNAME = "types.theme"

    def __init__(self, *, id: int, access_hash: int, slug: str, title: str, creator: Optional[bool] = None, default: Optional[bool] = None, for_chat: Optional[bool] = None, document: "api.ayiin.Document" = None, settings: Optional[List["api.ayiin.ThemeSettings"]] = None, emoticon: Optional[str] = None, installs_count: Optional[int] = None) -> None:
        
                self.id = id  # long
        
                self.access_hash = access_hash  # long
        
                self.slug = slug  # string
        
                self.title = title  # string
        
                self.creator = creator  # true
        
                self.default = default  # true
        
                self.for_chat = for_chat  # true
        
                self.document = document  # Document
        
                self.settings = settings  # ThemeSettings
        
                self.emoticon = emoticon  # string
        
                self.installs_count = installs_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Theme":
        
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        default = True if flags & (1 << 1) else False
        for_chat = True if flags & (1 << 5) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        slug = String.read(b)
        
        title = String.read(b)
        
        document = Object.read(b) if flags & (1 << 2) else None
        
        settings = Object.read(b) if flags & (1 << 3) else []
        
        emoticon = String.read(b) if flags & (1 << 6) else None
        installs_count = Int.read(b) if flags & (1 << 4) else None
        return Theme(id=id, access_hash=access_hash, slug=slug, title=title, creator=creator, default=default, for_chat=for_chat, document=document, settings=settings, emoticon=emoticon, installs_count=installs_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.slug))
        
        b.write(String(self.title))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.settings is not None:
            b.write(Vector(self.settings))
        
        if self.emoticon is not None:
            b.write(String(self.emoticon))
        
        if self.installs_count is not None:
            b.write(Int(self.installs_count))
        
        return b.getvalue()