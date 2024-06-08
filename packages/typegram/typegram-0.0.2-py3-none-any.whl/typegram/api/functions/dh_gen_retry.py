
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



class Dh_gen_retry(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``46DC1FB9``

nonce (``int`` ``128-bit``):
                    N/A
                
        server_nonce (``int`` ``128-bit``):
                    N/A
                
        new_nonce_hash2 (``int`` ``128-bit``):
                    N/A
                
    Returns:
        :obj:`Set_client_DH_params_answer<typegram.api.ayiin.Set_client_DH_params_answer>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "new_nonce_hash2"]

    ID = 0x46dc1fb9
    QUALNAME = "functions.dh_gen_retry"

    def __init__(self, *, nonce: int, server_nonce: int, new_nonce_hash2: int) -> None:
        
                self.nonce = nonce  # int128
        
                self.server_nonce = server_nonce  # int128
        
                self.new_nonce_hash2 = new_nonce_hash2  # int128

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Dh_gen_retry":
        # No flags
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        new_nonce_hash2 = Int128.read(b)
        
        return Dh_gen_retry(nonce=nonce, server_nonce=server_nonce, new_nonce_hash2=new_nonce_hash2)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Int128(self.new_nonce_hash2))
        
        return b.getvalue()