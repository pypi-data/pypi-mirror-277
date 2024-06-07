
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



class GetFullChat(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``AEB00B34``

chat_id (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`messages.ChatFull<typegram.api.ayiin.messages.ChatFull>`
    """

    __slots__: List[str] = ["chat_id"]

    ID = 0xaeb00b34
    QUALNAME = "functions.functionsmessages.ChatFull"

    def __init__(self, *, chat_id: int) -> None:
        
                self.chat_id = chat_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFullChat":
        # No flags
        
        chat_id = Long.read(b)
        
        return GetFullChat(chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        return b.getvalue()