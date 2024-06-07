
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



class EditChatTitle(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``73783FFD``

chat_id (``int`` ``64-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["chat_id", "title"]

    ID = 0x73783ffd
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, chat_id: int, title: str) -> None:
        
                self.chat_id = chat_id  # long
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatTitle":
        # No flags
        
        chat_id = Long.read(b)
        
        title = String.read(b)
        
        return EditChatTitle(chat_id=chat_id, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        b.write(String(self.title))
        
        return b.getvalue()