
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



class Set_client_DH_params(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F5045F1F``

nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        server_nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        encrypted_data (``str``):
                    N/A
                
    Returns:
        :obj:`Set_client_DH_params_answer<typegram.api.ayiin.Set_client_DH_params_answer>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "encrypted_data"]

    ID = 0xf5045f1f
    QUALNAME = "functions.functions.Set_client_DH_params_answer"

    def __init__(self, *, nonce: "ayiin.int128", server_nonce: "ayiin.int128", encrypted_data: str) -> None:
        
                self.nonce = nonce  # int128
        
                self.server_nonce = server_nonce  # int128
        
                self.encrypted_data = encrypted_data  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Set_client_DH_params":
        # No flags
        
        nonce = Object.read(b)
        
        server_nonce = Object.read(b)
        
        encrypted_data = String.read(b)
        
        return Set_client_DH_params(nonce=nonce, server_nonce=server_nonce, encrypted_data=encrypted_data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.nonce.write())
        
        b.write(self.server_nonce.write())
        
        b.write(String(self.encrypted_data))
        
        return b.getvalue()