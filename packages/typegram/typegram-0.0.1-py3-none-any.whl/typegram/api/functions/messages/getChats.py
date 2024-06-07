
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



class GetChats(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``49E9528F``

id (List of ``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`messages.Chats<typegram.api.ayiin.messages.Chats>`
    """

    __slots__: List[str] = ["id"]

    ID = 0x49e9528f
    QUALNAME = "functions.functionsmessages.Chats"

    def __init__(self, *, id: List[int]) -> None:
        
                self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChats":
        # No flags
        
        id = Object.read(b, Long)
        
        return GetChats(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id, Long))
        
        return b.getvalue()