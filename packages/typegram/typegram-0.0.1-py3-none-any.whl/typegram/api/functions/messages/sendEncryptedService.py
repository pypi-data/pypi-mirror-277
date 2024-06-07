
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



class SendEncryptedService(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``32D439A4``

peer (:obj:`InputEncryptedChat<typegram.api.ayiin.InputEncryptedChat>`):
                    N/A
                
        random_id (``int`` ``64-bit``):
                    N/A
                
        data (``bytes``):
                    N/A
                
    Returns:
        :obj:`messages.SentEncryptedMessage<typegram.api.ayiin.messages.SentEncryptedMessage>`
    """

    __slots__: List[str] = ["peer", "random_id", "data"]

    ID = 0x32d439a4
    QUALNAME = "functions.functionsmessages.SentEncryptedMessage"

    def __init__(self, *, peer: "ayiin.InputEncryptedChat", random_id: int, data: bytes) -> None:
        
                self.peer = peer  # InputEncryptedChat
        
                self.random_id = random_id  # long
        
                self.data = data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendEncryptedService":
        # No flags
        
        peer = Object.read(b)
        
        random_id = Long.read(b)
        
        data = Bytes.read(b)
        
        return SendEncryptedService(peer=peer, random_id=random_id, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.random_id))
        
        b.write(Bytes(self.data))
        
        return b.getvalue()