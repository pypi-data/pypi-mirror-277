
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



class Req_pq(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``60469778``

nonce (:obj:`int128<typegram.api.ayiin.int128>`):
                    N/A
                
    Returns:
        :obj:`ResPQ<typegram.api.ayiin.ResPQ>`
    """

    __slots__: List[str] = ["nonce"]

    ID = 0x60469778
    QUALNAME = "functions.functions.ResPQ"

    def __init__(self, *, nonce: "ayiin.int128") -> None:
        
                self.nonce = nonce  # int128

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Req_pq":
        # No flags
        
        nonce = Object.read(b)
        
        return Req_pq(nonce=nonce)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.nonce.write())
        
        return b.getvalue()