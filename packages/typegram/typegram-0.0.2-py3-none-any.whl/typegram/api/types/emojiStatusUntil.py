
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



class EmojiStatusUntil(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.EmojiStatus`.

    Details:
        - Layer: ``181``
        - ID: ``FA30A8C7``

document_id (``int`` ``64-bit``):
                    N/A
                
        until (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["document_id", "until"]

    ID = 0xfa30a8c7
    QUALNAME = "types.emojiStatusUntil"

    def __init__(self, *, document_id: int, until: int) -> None:
        
                self.document_id = document_id  # long
        
                self.until = until  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiStatusUntil":
        # No flags
        
        document_id = Long.read(b)
        
        until = Int.read(b)
        
        return EmojiStatusUntil(document_id=document_id, until=until)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.document_id))
        
        b.write(Int(self.until))
        
        return b.getvalue()