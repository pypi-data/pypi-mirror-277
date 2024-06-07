
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



class Dh_gen_fail(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A69DAE02``

nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        server_nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        new_nonce_hash3 (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
    Returns:
        :obj:`Set_client_DH_params_answer<typegram.api.ayiin.Set_client_DH_params_answer>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "new_nonce_hash3"]

    ID = 0xa69dae02
    QUALNAME = "functions.functions.Set_client_DH_params_answer"

    def __init__(self, *, nonce: "ayiin.int128", server_nonce: "ayiin.int128", new_nonce_hash3: "ayiin.int128") -> None:
        
                self.nonce = nonce  # int128
        
                self.server_nonce = server_nonce  # int128
        
                self.new_nonce_hash3 = new_nonce_hash3  # int128

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Dh_gen_fail":
        # No flags
        
        nonce = Object.read(b)
        
        server_nonce = Object.read(b)
        
        new_nonce_hash3 = Object.read(b)
        
        return Dh_gen_fail(nonce=nonce, server_nonce=server_nonce, new_nonce_hash3=new_nonce_hash3)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.nonce.write())
        
        b.write(self.server_nonce.write())
        
        b.write(self.new_nonce_hash3.write())
        
        return b.getvalue()