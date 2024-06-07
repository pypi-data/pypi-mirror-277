
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



class AppUpdate(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.AppUpdate`.

    Details:
        - Layer: ``181``
        - ID: ``CCBBCE30``

id (``int`` ``32-bit``):
                    N/A
                
        version (``str``):
                    N/A
                
        text (``str``):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`):
                    N/A
                
        can_not_skip (``bool``, *optional*):
                    N/A
                
        document (:obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
        url (``str``, *optional*):
                    N/A
                
        sticker (:obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            help.AppUpdate
            help.RecentMeUrls
            help.DeepLinkInfo
            help.AppConfig
            help.PassportConfig
            help.UserInfo
            help.CountriesList
            help.PeerColors
            help.TimezonesList
    """

    __slots__: List[str] = ["id", "version", "text", "entities", "can_not_skip", "document", "url", "sticker"]

    ID = 0xccbbce30
    QUALNAME = "functions.typeshelp.AppUpdate"

    def __init__(self, *, id: int, version: str, text: str, entities: List["ayiin.MessageEntity"], can_not_skip: Optional[bool] = None, document: "ayiin.Document" = None, url: Optional[str] = None, sticker: "ayiin.Document" = None) -> None:
        
                self.id = id  # int
        
                self.version = version  # string
        
                self.text = text  # string
        
                self.entities = entities  # MessageEntity
        
                self.can_not_skip = can_not_skip  # true
        
                self.document = document  # Document
        
                self.url = url  # string
        
                self.sticker = sticker  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppUpdate":
        
        flags = Int.read(b)
        
        can_not_skip = True if flags & (1 << 0) else False
        id = Int.read(b)
        
        version = String.read(b)
        
        text = String.read(b)
        
        entities = Object.read(b)
        
        document = Object.read(b) if flags & (1 << 1) else None
        
        url = String.read(b) if flags & (1 << 2) else None
        sticker = Object.read(b) if flags & (1 << 3) else None
        
        return AppUpdate(id=id, version=version, text=text, entities=entities, can_not_skip=can_not_skip, document=document, url=url, sticker=sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.version))
        
        b.write(String(self.text))
        
        b.write(Vector(self.entities))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.sticker is not None:
            b.write(self.sticker.write())
        
        return b.getvalue()