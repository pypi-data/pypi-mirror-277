
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



class MessageEntitySpoiler(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageEntity`.

    Details:
        - Layer: ``181``
        - ID: ``32CA960F``

offset (``int`` ``32-bit``):
                    N/A
                
        length (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["offset", "length"]

    ID = 0x32ca960f
    QUALNAME = "types.messageEntitySpoiler"

    def __init__(self, *, offset: int, length: int) -> None:
        
                self.offset = offset  # int
        
                self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntitySpoiler":
        # No flags
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        return MessageEntitySpoiler(offset=offset, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        return b.getvalue()