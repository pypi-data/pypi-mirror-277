
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



class UploadEncryptedFile(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``5057C497``

peer (:obj:`InputEncryptedChat<typegram.api.ayiin.InputEncryptedChat>`):
                    N/A
                
        file (:obj:`InputEncryptedFile<typegram.api.ayiin.InputEncryptedFile>`):
                    N/A
                
    Returns:
        :obj:`EncryptedFile<typegram.api.ayiin.EncryptedFile>`
    """

    __slots__: List[str] = ["peer", "file"]

    ID = 0x5057c497
    QUALNAME = "functions.functions.EncryptedFile"

    def __init__(self, *, peer: "ayiin.InputEncryptedChat", file: "ayiin.InputEncryptedFile") -> None:
        
                self.peer = peer  # InputEncryptedChat
        
                self.file = file  # InputEncryptedFile

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadEncryptedFile":
        # No flags
        
        peer = Object.read(b)
        
        file = Object.read(b)
        
        return UploadEncryptedFile(peer=peer, file=file)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.file.write())
        
        return b.getvalue()