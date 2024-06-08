
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



class EncryptedMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.EncryptedMessage`.

    Details:
        - Layer: ``181``
        - ID: ``ED18C118``

random_id (``int`` ``64-bit``):
                    N/A
                
        chat_id (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        bytes (``bytes``):
                    N/A
                
        file (:obj:`EncryptedFile<typegram.api.ayiin.EncryptedFile>`):
                    N/A
                
    """

    __slots__: List[str] = ["random_id", "chat_id", "date", "bytes", "file"]

    ID = 0xed18c118
    QUALNAME = "types.encryptedMessage"

    def __init__(self, *, random_id: int, chat_id: int, date: int, bytes: bytes, file: "api.ayiin.EncryptedFile") -> None:
        
                self.random_id = random_id  # long
        
                self.chat_id = chat_id  # int
        
                self.date = date  # int
        
                self.bytes = bytes  # bytes
        
                self.file = file  # EncryptedFile

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedMessage":
        # No flags
        
        random_id = Long.read(b)
        
        chat_id = Int.read(b)
        
        date = Int.read(b)
        
        bytes = Bytes.read(b)
        
        file = Object.read(b)
        
        return EncryptedMessage(random_id=random_id, chat_id=chat_id, date=date, bytes=bytes, file=file)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.random_id))
        
        b.write(Int(self.chat_id))
        
        b.write(Int(self.date))
        
        b.write(Bytes(self.bytes))
        
        b.write(self.file.write())
        
        return b.getvalue()