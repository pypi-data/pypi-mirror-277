
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



class EditInlineBotMessage(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``83557DBA``

id (:obj:`InputBotInlineMessageID<typegram.api.ayiin.InputBotInlineMessageID>`):
                    N/A
                
        no_webpage (``bool``, *optional*):
                    N/A
                
        invert_media (``bool``, *optional*):
                    N/A
                
        message (``str``, *optional*):
                    N/A
                
        media (:obj:`InputMedia<typegram.api.ayiin.InputMedia>`, *optional*):
                    N/A
                
        reply_markup (:obj:`ReplyMarkup<typegram.api.ayiin.ReplyMarkup>`, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "no_webpage", "invert_media", "message", "media", "reply_markup", "entities"]

    ID = 0x83557dba
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, id: "ayiin.InputBotInlineMessageID", no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, message: Optional[str] = None, media: "ayiin.InputMedia" = None, reply_markup: "ayiin.ReplyMarkup" = None, entities: Optional[List["ayiin.MessageEntity"]] = None) -> None:
        
                self.id = id  # InputBotInlineMessageID
        
                self.no_webpage = no_webpage  # true
        
                self.invert_media = invert_media  # true
        
                self.message = message  # string
        
                self.media = media  # InputMedia
        
                self.reply_markup = reply_markup  # ReplyMarkup
        
                self.entities = entities  # MessageEntity

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditInlineBotMessage":
        
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 1) else False
        invert_media = True if flags & (1 << 16) else False
        id = Object.read(b)
        
        message = String.read(b) if flags & (1 << 11) else None
        media = Object.read(b) if flags & (1 << 14) else None
        
        reply_markup = Object.read(b) if flags & (1 << 2) else None
        
        entities = Object.read(b) if flags & (1 << 3) else []
        
        return EditInlineBotMessage(id=id, no_webpage=no_webpage, invert_media=invert_media, message=message, media=media, reply_markup=reply_markup, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        return b.getvalue()