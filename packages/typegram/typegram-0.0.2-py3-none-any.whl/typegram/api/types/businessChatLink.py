
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



class BusinessChatLink(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BusinessChatLink`.

    Details:
        - Layer: ``181``
        - ID: ``B4AE666F``

link (``str``):
                    N/A
                
        message (``str``):
                    N/A
                
        views (``int`` ``32-bit``):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            account.createBusinessChatLink
            account.editBusinessChatLink
    """

    __slots__: List[str] = ["link", "message", "views", "entities", "title"]

    ID = 0xb4ae666f
    QUALNAME = "types.businessChatLink"

    def __init__(self, *, link: str, message: str, views: int, entities: Optional[List["api.ayiin.MessageEntity"]] = None, title: Optional[str] = None) -> None:
        
                self.link = link  # string
        
                self.message = message  # string
        
                self.views = views  # int
        
                self.entities = entities  # MessageEntity
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessChatLink":
        
        flags = Int.read(b)
        
        link = String.read(b)
        
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 0) else []
        
        title = String.read(b) if flags & (1 << 1) else None
        views = Int.read(b)
        
        return BusinessChatLink(link=link, message=message, views=views, entities=entities, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.link))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.title is not None:
            b.write(String(self.title))
        
        b.write(Int(self.views))
        
        return b.getvalue()