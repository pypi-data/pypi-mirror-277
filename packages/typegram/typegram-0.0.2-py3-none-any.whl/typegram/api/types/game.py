
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



class Game(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Game`.

    Details:
        - Layer: ``181``
        - ID: ``BDF9653B``

id (``int`` ``64-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        short_name (``str``):
                    N/A
                
        title (``str``):
                    N/A
                
        description (``str``):
                    N/A
                
        photo (:obj:`Photo<typegram.api.ayiin.Photo>`):
                    N/A
                
        document (:obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "access_hash", "short_name", "title", "description", "photo", "document"]

    ID = 0xbdf9653b
    QUALNAME = "types.game"

    def __init__(self, *, id: int, access_hash: int, short_name: str, title: str, description: str, photo: "api.ayiin.Photo", document: "api.ayiin.Document" = None) -> None:
        
                self.id = id  # long
        
                self.access_hash = access_hash  # long
        
                self.short_name = short_name  # string
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.photo = photo  # Photo
        
                self.document = document  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Game":
        
        flags = Int.read(b)
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        short_name = String.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = Object.read(b)
        
        document = Object.read(b) if flags & (1 << 0) else None
        
        return Game(id=id, access_hash=access_hash, short_name=short_name, title=title, description=description, photo=photo, document=document)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.short_name))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        b.write(self.photo.write())
        
        if self.document is not None:
            b.write(self.document.write())
        
        return b.getvalue()