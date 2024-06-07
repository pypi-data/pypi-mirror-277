
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



class GetWebPagePreview(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8B68B0CC``

message (``str``):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
    Returns:
        :obj:`MessageMedia<typegram.api.ayiin.MessageMedia>`
    """

    __slots__: List[str] = ["message", "entities"]

    ID = 0x8b68b0cc
    QUALNAME = "functions.functions.MessageMedia"

    def __init__(self, *, message: str, entities: Optional[List["ayiin.MessageEntity"]] = None) -> None:
        
                self.message = message  # string
        
                self.entities = entities  # MessageEntity

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWebPagePreview":
        
        flags = Int.read(b)
        
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 3) else []
        
        return GetWebPagePreview(message=message, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        return b.getvalue()