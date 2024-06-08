
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



class Req_pq_multi(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``BE7E8EF1``

nonce (``int`` ``128-bit``):
                    N/A
                
    Returns:
        :obj:`ResPQ<typegram.api.ayiin.ResPQ>`
    """

    __slots__: List[str] = ["nonce"]

    ID = 0xbe7e8ef1
    QUALNAME = "functions.req_pq_multi"

    def __init__(self, *, nonce: int) -> None:
        
                self.nonce = nonce  # int128

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Req_pq_multi":
        # No flags
        
        nonce = Int128.read(b)
        
        return Req_pq_multi(nonce=nonce)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        return b.getvalue()