
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



class DiscardEncryption(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F393AEA0``

chat_id (``int`` ``32-bit``):
                    N/A
                
        delete_history (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["chat_id", "delete_history"]

    ID = 0xf393aea0
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, chat_id: int, delete_history: Optional[bool] = None) -> None:
        
                self.chat_id = chat_id  # int
        
                self.delete_history = delete_history  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DiscardEncryption":
        
        flags = Int.read(b)
        
        delete_history = True if flags & (1 << 0) else False
        chat_id = Int.read(b)
        
        return DiscardEncryption(chat_id=chat_id, delete_history=delete_history)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.chat_id))
        
        return b.getvalue()