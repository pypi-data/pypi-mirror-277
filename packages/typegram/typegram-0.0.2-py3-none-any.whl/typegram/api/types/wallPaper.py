
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



class WallPaper(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WallPaper`.

    Details:
        - Layer: ``181``
        - ID: ``A437C3ED``

id (``int`` ``64-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        slug (``str``):
                    N/A
                
        document (:obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
        creator (``bool``, *optional*):
                    N/A
                
        default (``bool``, *optional*):
                    N/A
                
        pattern (``bool``, *optional*):
                    N/A
                
        dark (``bool``, *optional*):
                    N/A
                
        settings (:obj:`WallPaperSettings<typegram.api.ayiin.WallPaperSettings>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 9 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            account.getWallPaper
            account.uploadWallPaper
            account.getMultiWallPapers
    """

    __slots__: List[str] = ["id", "access_hash", "slug", "document", "creator", "default", "pattern", "dark", "settings"]

    ID = 0xa437c3ed
    QUALNAME = "types.wallPaper"

    def __init__(self, *, id: int, access_hash: int, slug: str, document: "api.ayiin.Document", creator: Optional[bool] = None, default: Optional[bool] = None, pattern: Optional[bool] = None, dark: Optional[bool] = None, settings: "api.ayiin.WallPaperSettings" = None) -> None:
        
                self.id = id  # long
        
                self.access_hash = access_hash  # long
        
                self.slug = slug  # string
        
                self.document = document  # Document
        
                self.creator = creator  # true
        
                self.default = default  # true
        
                self.pattern = pattern  # true
        
                self.dark = dark  # true
        
                self.settings = settings  # WallPaperSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WallPaper":
        
        id = Long.read(b)
        
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        default = True if flags & (1 << 1) else False
        pattern = True if flags & (1 << 3) else False
        dark = True if flags & (1 << 4) else False
        access_hash = Long.read(b)
        
        slug = String.read(b)
        
        document = Object.read(b)
        
        settings = Object.read(b) if flags & (1 << 2) else None
        
        return WallPaper(id=id, access_hash=access_hash, slug=slug, document=document, creator=creator, default=default, pattern=pattern, dark=dark, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.slug))
        
        b.write(self.document.write())
        
        if self.settings is not None:
            b.write(self.settings.write())
        
        return b.getvalue()