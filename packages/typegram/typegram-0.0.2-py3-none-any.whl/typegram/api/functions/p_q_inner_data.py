
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



class P_q_inner_data(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``83C95AEC``

pq (``str``):
                    N/A
                
        p (``str``):
                    N/A
                
        q (``str``):
                    N/A
                
        nonce (``int`` ``128-bit``):
                    N/A
                
        server_nonce (``int`` ``128-bit``):
                    N/A
                
        new_nonce (``int`` ``256-bit``):
                    N/A
                
    Returns:
        :obj:`P_Q_inner_data<typegram.api.ayiin.P_Q_inner_data>`
    """

    __slots__: List[str] = ["pq", "p", "q", "nonce", "server_nonce", "new_nonce"]

    ID = 0x83c95aec
    QUALNAME = "functions.p_q_inner_data"

    def __init__(self, *, pq: str, p: str, q: str, nonce: int, server_nonce: int, new_nonce: int) -> None:
        
                self.pq = pq  # string
        
                self.p = p  # string
        
                self.q = q  # string
        
                self.nonce = nonce  # int128
        
                self.server_nonce = server_nonce  # int128
        
                self.new_nonce = new_nonce  # int256

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "P_q_inner_data":
        # No flags
        
        pq = String.read(b)
        
        p = String.read(b)
        
        q = String.read(b)
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        new_nonce = Int256.read(b)
        
        return P_q_inner_data(pq=pq, p=p, q=q, nonce=nonce, server_nonce=server_nonce, new_nonce=new_nonce)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.pq))
        
        b.write(String(self.p))
        
        b.write(String(self.q))
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Int256(self.new_nonce))
        
        return b.getvalue()