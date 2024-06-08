
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



class Req_DH_params(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D712E4BE``

nonce (``int`` ``128-bit``):
                    N/A
                
        server_nonce (``int`` ``128-bit``):
                    N/A
                
        p (``str``):
                    N/A
                
        q (``str``):
                    N/A
                
        public_key_fingerprint (``int`` ``64-bit``):
                    N/A
                
        encrypted_data (``str``):
                    N/A
                
    Returns:
        :obj:`Server_DH_Params<typegram.api.ayiin.Server_DH_Params>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "p", "q", "public_key_fingerprint", "encrypted_data"]

    ID = 0xd712e4be
    QUALNAME = "functions.req_DH_params"

    def __init__(self, *, nonce: int, server_nonce: int, p: str, q: str, public_key_fingerprint: int, encrypted_data: str) -> None:
        
                self.nonce = nonce  # int128
        
                self.server_nonce = server_nonce  # int128
        
                self.p = p  # string
        
                self.q = q  # string
        
                self.public_key_fingerprint = public_key_fingerprint  # long
        
                self.encrypted_data = encrypted_data  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Req_DH_params":
        # No flags
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        p = String.read(b)
        
        q = String.read(b)
        
        public_key_fingerprint = Long.read(b)
        
        encrypted_data = String.read(b)
        
        return Req_DH_params(nonce=nonce, server_nonce=server_nonce, p=p, q=q, public_key_fingerprint=public_key_fingerprint, encrypted_data=encrypted_data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(String(self.p))
        
        b.write(String(self.q))
        
        b.write(Long(self.public_key_fingerprint))
        
        b.write(String(self.encrypted_data))
        
        return b.getvalue()