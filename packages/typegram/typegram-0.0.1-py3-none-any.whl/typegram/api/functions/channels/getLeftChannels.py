
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



class GetLeftChannels(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8341ECC0``

offset (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.Chats<typegram.api.ayiin.messages.Chats>`
    """

    __slots__: List[str] = ["offset"]

    ID = 0x8341ecc0
    QUALNAME = "functions.functionsmessages.Chats"

    def __init__(self, *, offset: int) -> None:
        
                self.offset = offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetLeftChannels":
        # No flags
        
        offset = Int.read(b)
        
        return GetLeftChannels(offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        return b.getvalue()