
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



class BotInlineMessageText(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BotInlineMessage`.

    Details:
        - Layer: ``181``
        - ID: ``8C7F65E2``

message (``str``):
                    N/A
                
        no_webpage (``bool``, *optional*):
                    N/A
                
        invert_media (``bool``, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        reply_markup (:obj:`ReplyMarkup<typegram.api.ayiin.ReplyMarkup>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["message", "no_webpage", "invert_media", "entities", "reply_markup"]

    ID = 0x8c7f65e2
    QUALNAME = "types.botInlineMessageText"

    def __init__(self, *, message: str, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, entities: Optional[List["api.ayiin.MessageEntity"]] = None, reply_markup: "api.ayiin.ReplyMarkup" = None) -> None:
        
                self.message = message  # string
        
                self.no_webpage = no_webpage  # true
        
                self.invert_media = invert_media  # true
        
                self.entities = entities  # MessageEntity
        
                self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMessageText":
        
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 0) else False
        invert_media = True if flags & (1 << 3) else False
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 1) else []
        
        reply_markup = Object.read(b) if flags & (1 << 2) else None
        
        return BotInlineMessageText(message=message, no_webpage=no_webpage, invert_media=invert_media, entities=entities, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()