
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



class MessageEntityPre(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageEntity`.

    Details:
        - Layer: ``181``
        - ID: ``73924BE0``

offset (``int`` ``32-bit``):
                    N/A
                
        length (``int`` ``32-bit``):
                    N/A
                
        language (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["offset", "length", "language"]

    ID = 0x73924be0
    QUALNAME = "types.messageEntityPre"

    def __init__(self, *, offset: int, length: int, language: str) -> None:
        
                self.offset = offset  # int
        
                self.length = length  # int
        
                self.language = language  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityPre":
        # No flags
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        language = String.read(b)
        
        return MessageEntityPre(offset=offset, length=length, language=language)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        b.write(String(self.language))
        
        return b.getvalue()