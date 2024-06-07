
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



class ResPQ(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``05162463``

nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        server_nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        pq (``str``):
                    N/A
                
        server_public_key_fingerprints (List of ``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`ResPQ<typegram.api.ayiin.ResPQ>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "pq", "server_public_key_fingerprints"]

    ID = 0x05162463
    QUALNAME = "functions.functions.ResPQ"

    def __init__(self, *, nonce: "ayiin.int128", server_nonce: "ayiin.int128", pq: str, server_public_key_fingerprints: List[int]) -> None:
        
                self.nonce = nonce  # int128
        
                self.server_nonce = server_nonce  # int128
        
                self.pq = pq  # string
        
                self.server_public_key_fingerprints = server_public_key_fingerprints  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResPQ":
        # No flags
        
        nonce = Object.read(b)
        
        server_nonce = Object.read(b)
        
        pq = String.read(b)
        
        server_public_key_fingerprints = Object.read(b, Long)
        
        return ResPQ(nonce=nonce, server_nonce=server_nonce, pq=pq, server_public_key_fingerprints=server_public_key_fingerprints)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.nonce.write())
        
        b.write(self.server_nonce.write())
        
        b.write(String(self.pq))
        
        b.write(Vector(self.server_public_key_fingerprints, Long))
        
        return b.getvalue()