
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



class MessageEntityCustomEmoji(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageEntity`.

    Details:
        - Layer: ``181``
        - ID: ``C8CF05F8``

offset (``int`` ``32-bit``):
                    N/A
                
        length (``int`` ``32-bit``):
                    N/A
                
        document_id (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["offset", "length", "document_id"]

    ID = 0xc8cf05f8
    QUALNAME = "types.messageEntityCustomEmoji"

    def __init__(self, *, offset: int, length: int, document_id: int) -> None:
        
                self.offset = offset  # int
        
                self.length = length  # int
        
                self.document_id = document_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityCustomEmoji":
        # No flags
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        document_id = Long.read(b)
        
        return MessageEntityCustomEmoji(offset=offset, length=length, document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        b.write(Long(self.document_id))
        
        return b.getvalue()