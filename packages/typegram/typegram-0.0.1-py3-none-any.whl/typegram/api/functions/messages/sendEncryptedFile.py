
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



class SendEncryptedFile(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``5559481D``

peer (:obj:`InputEncryptedChat<typegram.api.ayiin.InputEncryptedChat>`):
                    N/A
                
        random_id (``int`` ``64-bit``):
                    N/A
                
        data (``bytes``):
                    N/A
                
        file (:obj:`InputEncryptedFile<typegram.api.ayiin.InputEncryptedFile>`):
                    N/A
                
        silent (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.SentEncryptedMessage<typegram.api.ayiin.messages.SentEncryptedMessage>`
    """

    __slots__: List[str] = ["peer", "random_id", "data", "file", "silent"]

    ID = 0x5559481d
    QUALNAME = "functions.functionsmessages.SentEncryptedMessage"

    def __init__(self, *, peer: "ayiin.InputEncryptedChat", random_id: int, data: bytes, file: "ayiin.InputEncryptedFile", silent: Optional[bool] = None) -> None:
        
                self.peer = peer  # InputEncryptedChat
        
                self.random_id = random_id  # long
        
                self.data = data  # bytes
        
                self.file = file  # InputEncryptedFile
        
                self.silent = silent  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendEncryptedFile":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        random_id = Long.read(b)
        
        data = Bytes.read(b)
        
        file = Object.read(b)
        
        return SendEncryptedFile(peer=peer, random_id=random_id, data=data, file=file, silent=silent)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Long(self.random_id))
        
        b.write(Bytes(self.data))
        
        b.write(self.file.write())
        
        return b.getvalue()