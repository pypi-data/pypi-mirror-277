
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



class InputBotInlineMessageMediaWebPage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBotInlineMessage`.

    Details:
        - Layer: ``181``
        - ID: ``BDDCC510``

message (``str``):
                    N/A
                
        url (``str``):
                    N/A
                
        invert_media (``bool``, *optional*):
                    N/A
                
        force_large_media (``bool``, *optional*):
                    N/A
                
        force_small_media (``bool``, *optional*):
                    N/A
                
        optional (``bool``, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        reply_markup (:obj:`ReplyMarkup<typegram.api.ayiin.ReplyMarkup>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["message", "url", "invert_media", "force_large_media", "force_small_media", "optional", "entities", "reply_markup"]

    ID = 0xbddcc510
    QUALNAME = "types.inputBotInlineMessageMediaWebPage"

    def __init__(self, *, message: str, url: str, invert_media: Optional[bool] = None, force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, optional: Optional[bool] = None, entities: Optional[List["api.ayiin.MessageEntity"]] = None, reply_markup: "api.ayiin.ReplyMarkup" = None) -> None:
        
                self.message = message  # string
        
                self.url = url  # string
        
                self.invert_media = invert_media  # true
        
                self.force_large_media = force_large_media  # true
        
                self.force_small_media = force_small_media  # true
        
                self.optional = optional  # true
        
                self.entities = entities  # MessageEntity
        
                self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageMediaWebPage":
        
        flags = Int.read(b)
        
        invert_media = True if flags & (1 << 3) else False
        force_large_media = True if flags & (1 << 4) else False
        force_small_media = True if flags & (1 << 5) else False
        optional = True if flags & (1 << 6) else False
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 1) else []
        
        url = String.read(b)
        
        reply_markup = Object.read(b) if flags & (1 << 2) else None
        
        return InputBotInlineMessageMediaWebPage(message=message, url=url, invert_media=invert_media, force_large_media=force_large_media, force_small_media=force_small_media, optional=optional, entities=entities, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        b.write(String(self.url))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()