
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



class P_q_inner_data_temp(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3C6A84D4``

pq (``str``):
                    N/A
                
        p (``str``):
                    N/A
                
        q (``str``):
                    N/A
                
        nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        server_nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        new_nonce (:obj:`int256<typegram.api.ayiin.int256>`):
                    N/A
                
        expires_in (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`P_Q_inner_data<typegram.api.ayiin.P_Q_inner_data>`
    """

    __slots__: List[str] = ["pq", "p", "q", "nonce", "server_nonce", "new_nonce", "expires_in"]

    ID = 0x3c6a84d4
    QUALNAME = "functions.functions.P_Q_inner_data"

    def __init__(self, *, pq: str, p: str, q: str, nonce: "ayiin.int128", server_nonce: "ayiin.int128", new_nonce: "ayiin.int256", expires_in: int) -> None:
        
                self.pq = pq  # string
        
                self.p = p  # string
        
                self.q = q  # string
        
                self.nonce = nonce  # int128
        
                self.server_nonce = server_nonce  # int128
        
                self.new_nonce = new_nonce  # int256
        
                self.expires_in = expires_in  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "P_q_inner_data_temp":
        # No flags
        
        pq = String.read(b)
        
        p = String.read(b)
        
        q = String.read(b)
        
        nonce = Object.read(b)
        
        server_nonce = Object.read(b)
        
        new_nonce = Object.read(b)
        
        expires_in = Int.read(b)
        
        return P_q_inner_data_temp(pq=pq, p=p, q=q, nonce=nonce, server_nonce=server_nonce, new_nonce=new_nonce, expires_in=expires_in)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.pq))
        
        b.write(String(self.p))
        
        b.write(String(self.q))
        
        b.write(self.nonce.write())
        
        b.write(self.server_nonce.write())
        
        b.write(self.new_nonce.write())
        
        b.write(Int(self.expires_in))
        
        return b.getvalue()