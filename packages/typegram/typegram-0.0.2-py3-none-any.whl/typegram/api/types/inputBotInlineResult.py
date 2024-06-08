
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



class InputBotInlineResult(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBotInlineResult`.

    Details:
        - Layer: ``181``
        - ID: ``88BF9319``

id (``str``):
                    N/A
                
        type (``str``):
                    N/A
                
        send_message (:obj:`InputBotInlineMessage<typegram.api.ayiin.InputBotInlineMessage>`):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        description (``str``, *optional*):
                    N/A
                
        url (``str``, *optional*):
                    N/A
                
        thumb (:obj:`InputWebDocument<typegram.api.ayiin.InputWebDocument>`, *optional*):
                    N/A
                
        content (:obj:`InputWebDocument<typegram.api.ayiin.InputWebDocument>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "type", "send_message", "title", "description", "url", "thumb", "content"]

    ID = 0x88bf9319
    QUALNAME = "types.inputBotInlineResult"

    def __init__(self, *, id: str, type: str, send_message: "api.ayiin.InputBotInlineMessage", title: Optional[str] = None, description: Optional[str] = None, url: Optional[str] = None, thumb: "api.ayiin.InputWebDocument" = None, content: "api.ayiin.InputWebDocument" = None) -> None:
        
                self.id = id  # string
        
                self.type = type  # string
        
                self.send_message = send_message  # InputBotInlineMessage
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.url = url  # string
        
                self.thumb = thumb  # InputWebDocument
        
                self.content = content  # InputWebDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineResult":
        
        flags = Int.read(b)
        
        id = String.read(b)
        
        type = String.read(b)
        
        title = String.read(b) if flags & (1 << 1) else None
        description = String.read(b) if flags & (1 << 2) else None
        url = String.read(b) if flags & (1 << 3) else None
        thumb = Object.read(b) if flags & (1 << 4) else None
        
        content = Object.read(b) if flags & (1 << 5) else None
        
        send_message = Object.read(b)
        
        return InputBotInlineResult(id=id, type=type, send_message=send_message, title=title, description=description, url=url, thumb=thumb, content=content)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        b.write(String(self.type))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        if self.content is not None:
            b.write(self.content.write())
        
        b.write(self.send_message.write())
        
        return b.getvalue()