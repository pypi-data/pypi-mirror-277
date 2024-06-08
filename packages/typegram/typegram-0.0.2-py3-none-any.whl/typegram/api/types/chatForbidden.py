
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



class ChatForbidden(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Chat`.

    Details:
        - Layer: ``181``
        - ID: ``6592A1A7``

id (``int`` ``64-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["id", "title"]

    ID = 0x6592a1a7
    QUALNAME = "types.chatForbidden"

    def __init__(self, *, id: int, title: str) -> None:
        
                self.id = id  # long
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatForbidden":
        # No flags
        
        id = Long.read(b)
        
        title = String.read(b)
        
        return ChatForbidden(id=id, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(String(self.title))
        
        return b.getvalue()