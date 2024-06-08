
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



class InputMediaDocument(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputMedia`.

    Details:
        - Layer: ``181``
        - ID: ``33473058``

id (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`):
                    N/A
                
        spoiler (``bool``, *optional*):
                    N/A
                
        ttl_seconds (``int`` ``32-bit``, *optional*):
                    N/A
                
        query (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "spoiler", "ttl_seconds", "query"]

    ID = 0x33473058
    QUALNAME = "types.inputMediaDocument"

    def __init__(self, *, id: "api.ayiin.InputDocument", spoiler: Optional[bool] = None, ttl_seconds: Optional[int] = None, query: Optional[str] = None) -> None:
        
                self.id = id  # InputDocument
        
                self.spoiler = spoiler  # true
        
                self.ttl_seconds = ttl_seconds  # int
        
                self.query = query  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaDocument":
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 2) else False
        id = Object.read(b)
        
        ttl_seconds = Int.read(b) if flags & (1 << 0) else None
        query = String.read(b) if flags & (1 << 1) else None
        return InputMediaDocument(id=id, spoiler=spoiler, ttl_seconds=ttl_seconds, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        if self.query is not None:
            b.write(String(self.query))
        
        return b.getvalue()