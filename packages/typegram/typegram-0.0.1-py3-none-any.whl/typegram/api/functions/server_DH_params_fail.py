
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



class Server_DH_params_fail(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``79CB045D``

nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        server_nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        new_nonce_hash (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
    Returns:
        :obj:`Server_DH_Params<typegram.api.ayiin.Server_DH_Params>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "new_nonce_hash"]

    ID = 0x79cb045d
    QUALNAME = "functions.functions.Server_DH_Params"

    def __init__(self, *, nonce: "ayiin.int128", server_nonce: "ayiin.int128", new_nonce_hash: "ayiin.int128") -> None:
        
                self.nonce = nonce  # int128
        
                self.server_nonce = server_nonce  # int128
        
                self.new_nonce_hash = new_nonce_hash  # int128

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Server_DH_params_fail":
        # No flags
        
        nonce = Object.read(b)
        
        server_nonce = Object.read(b)
        
        new_nonce_hash = Object.read(b)
        
        return Server_DH_params_fail(nonce=nonce, server_nonce=server_nonce, new_nonce_hash=new_nonce_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.nonce.write())
        
        b.write(self.server_nonce.write())
        
        b.write(self.new_nonce_hash.write())
        
        return b.getvalue()