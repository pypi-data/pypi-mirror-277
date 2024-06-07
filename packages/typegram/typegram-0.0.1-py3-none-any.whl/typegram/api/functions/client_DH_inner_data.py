
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



class Client_DH_inner_data(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``6643B654``

nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        server_nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
        retry_id (``int`` ``64-bit``):
                    N/A
                
        g_b (``str``):
                    N/A
                
    Returns:
        :obj:`Client_DH_Inner_Data<typegram.api.ayiin.Client_DH_Inner_Data>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "retry_id", "g_b"]

    ID = 0x6643b654
    QUALNAME = "functions.functions.Client_DH_Inner_Data"

    def __init__(self, *, nonce: "ayiin.int128", server_nonce: "ayiin.int128", retry_id: int, g_b: str) -> None:
        
                self.nonce = nonce  # int128
        
                self.server_nonce = server_nonce  # int128
        
                self.retry_id = retry_id  # long
        
                self.g_b = g_b  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Client_DH_inner_data":
        # No flags
        
        nonce = Object.read(b)
        
        server_nonce = Object.read(b)
        
        retry_id = Long.read(b)
        
        g_b = String.read(b)
        
        return Client_DH_inner_data(nonce=nonce, server_nonce=server_nonce, retry_id=retry_id, g_b=g_b)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.nonce.write())
        
        b.write(self.server_nonce.write())
        
        b.write(Long(self.retry_id))
        
        b.write(String(self.g_b))
        
        return b.getvalue()