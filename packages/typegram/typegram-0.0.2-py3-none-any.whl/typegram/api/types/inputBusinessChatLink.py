
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



class InputBusinessChatLink(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBusinessChatLink`.

    Details:
        - Layer: ``181``
        - ID: ``11679FA7``

message (``str``):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["message", "entities", "title"]

    ID = 0x11679fa7
    QUALNAME = "types.inputBusinessChatLink"

    def __init__(self, *, message: str, entities: Optional[List["api.ayiin.MessageEntity"]] = None, title: Optional[str] = None) -> None:
        
                self.message = message  # string
        
                self.entities = entities  # MessageEntity
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBusinessChatLink":
        
        flags = Int.read(b)
        
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 0) else []
        
        title = String.read(b) if flags & (1 << 1) else None
        return InputBusinessChatLink(message=message, entities=entities, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.title is not None:
            b.write(String(self.title))
        
        return b.getvalue()