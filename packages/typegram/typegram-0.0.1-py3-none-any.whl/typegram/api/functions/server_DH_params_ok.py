
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



class Server_DH_params_ok(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D0E8075C``

nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        server_nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        encrypted_answer (``str``):
                    N/A
                
    Returns:
        :obj:`Server_DH_Params<typegram.api.ayiin.Server_DH_Params>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "encrypted_answer"]

    ID = 0xd0e8075c
    QUALNAME = "functions.functions.Server_DH_Params"

    def __init__(self, *, nonce: "ayiin.int128", server_nonce: "ayiin.int128", encrypted_answer: str) -> None:
        
                self.nonce = nonce  # int128
        
                self.server_nonce = server_nonce  # int128
        
                self.encrypted_answer = encrypted_answer  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Server_DH_params_ok":
        # No flags
        
        nonce = Object.read(b)
        
        server_nonce = Object.read(b)
        
        encrypted_answer = String.read(b)
        
        return Server_DH_params_ok(nonce=nonce, server_nonce=server_nonce, encrypted_answer=encrypted_answer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.nonce.write())
        
        b.write(self.server_nonce.write())
        
        b.write(String(self.encrypted_answer))
        
        return b.getvalue()