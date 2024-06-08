
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



class Server_DH_inner_data(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B5890DBA``

nonce (``int`` ``128-bit``):
                    N/A
                
        server_nonce (``int`` ``128-bit``):
                    N/A
                
        g (``int`` ``32-bit``):
                    N/A
                
        dh_prime (``str``):
                    N/A
                
        g_a (``str``):
                    N/A
                
        server_time (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`Server_DH_inner_data<typegram.api.ayiin.Server_DH_inner_data>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "g", "dh_prime", "g_a", "server_time"]

    ID = 0xb5890dba
    QUALNAME = "functions.server_DH_inner_data"

    def __init__(self, *, nonce: int, server_nonce: int, g: int, dh_prime: str, g_a: str, server_time: int) -> None:
        
                self.nonce = nonce  # int128
        
                self.server_nonce = server_nonce  # int128
        
                self.g = g  # int
        
                self.dh_prime = dh_prime  # string
        
                self.g_a = g_a  # string
        
                self.server_time = server_time  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Server_DH_inner_data":
        # No flags
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        g = Int.read(b)
        
        dh_prime = String.read(b)
        
        g_a = String.read(b)
        
        server_time = Int.read(b)
        
        return Server_DH_inner_data(nonce=nonce, server_nonce=server_nonce, g=g, dh_prime=dh_prime, g_a=g_a, server_time=server_time)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Int(self.g))
        
        b.write(String(self.dh_prime))
        
        b.write(String(self.g_a))
        
        b.write(Int(self.server_time))
        
        return b.getvalue()