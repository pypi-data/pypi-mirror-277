
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



class InputBotInlineResultDocument(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBotInlineResult`.

    Details:
        - Layer: ``181``
        - ID: ``FFF8FDC4``

id (``str``):
                    N/A
                
        type (``str``):
                    N/A
                
        document (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`):
                    N/A
                
        send_message (:obj:`InputBotInlineMessage<typegram.api.ayiin.InputBotInlineMessage>`):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        description (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "type", "document", "send_message", "title", "description"]

    ID = 0xfff8fdc4
    QUALNAME = "types.inputBotInlineResultDocument"

    def __init__(self, *, id: str, type: str, document: "api.ayiin.InputDocument", send_message: "api.ayiin.InputBotInlineMessage", title: Optional[str] = None, description: Optional[str] = None) -> None:
        
                self.id = id  # string
        
                self.type = type  # string
        
                self.document = document  # InputDocument
        
                self.send_message = send_message  # InputBotInlineMessage
        
                self.title = title  # string
        
                self.description = description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineResultDocument":
        
        flags = Int.read(b)
        
        id = String.read(b)
        
        type = String.read(b)
        
        title = String.read(b) if flags & (1 << 1) else None
        description = String.read(b) if flags & (1 << 2) else None
        document = Object.read(b)
        
        send_message = Object.read(b)
        
        return InputBotInlineResultDocument(id=id, type=type, document=document, send_message=send_message, title=title, description=description)

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
        
        b.write(self.document.write())
        
        b.write(self.send_message.write())
        
        return b.getvalue()