
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



class BotInfo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BotInfo`.

    Details:
        - Layer: ``181``
        - ID: ``8F300B57``

user_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        description (``str``, *optional*):
                    N/A
                
        description_photo (:obj:`Photo<typegram.api.ayiin.Photo>`, *optional*):
                    N/A
                
        description_document (:obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
        commands (List of :obj:`BotCommand<typegram.api.ayiin.BotCommand>`, *optional*):
                    N/A
                
        menu_button (:obj:`BotMenuButton<typegram.api.ayiin.BotMenuButton>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["user_id", "description", "description_photo", "description_document", "commands", "menu_button"]

    ID = 0x8f300b57
    QUALNAME = "types.botInfo"

    def __init__(self, *, user_id: Optional[int] = None, description: Optional[str] = None, description_photo: "api.ayiin.Photo" = None, description_document: "api.ayiin.Document" = None, commands: Optional[List["api.ayiin.BotCommand"]] = None, menu_button: "api.ayiin.BotMenuButton" = None) -> None:
        
                self.user_id = user_id  # long
        
                self.description = description  # string
        
                self.description_photo = description_photo  # Photo
        
                self.description_document = description_document  # Document
        
                self.commands = commands  # BotCommand
        
                self.menu_button = menu_button  # BotMenuButton

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInfo":
        
        flags = Int.read(b)
        
        user_id = Long.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        description_photo = Object.read(b) if flags & (1 << 4) else None
        
        description_document = Object.read(b) if flags & (1 << 5) else None
        
        commands = Object.read(b) if flags & (1 << 2) else []
        
        menu_button = Object.read(b) if flags & (1 << 3) else None
        
        return BotInfo(user_id=user_id, description=description, description_photo=description_photo, description_document=description_document, commands=commands, menu_button=menu_button)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.user_id is not None:
            b.write(Long(self.user_id))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.description_photo is not None:
            b.write(self.description_photo.write())
        
        if self.description_document is not None:
            b.write(self.description_document.write())
        
        if self.commands is not None:
            b.write(Vector(self.commands))
        
        if self.menu_button is not None:
            b.write(self.menu_button.write())
        
        return b.getvalue()