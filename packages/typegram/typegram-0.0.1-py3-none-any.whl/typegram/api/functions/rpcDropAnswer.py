
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



class RpcDropAnswer(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``58E4A740``

req_msg_id (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`RpcDropAnswer<typegram.api.ayiin.RpcDropAnswer>`
    """

    __slots__: List[str] = ["req_msg_id"]

    ID = 0x58e4a740
    QUALNAME = "functions.functions.RpcDropAnswer"

    def __init__(self, *, req_msg_id: int) -> None:
        
                self.req_msg_id = req_msg_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RpcDropAnswer":
        # No flags
        
        req_msg_id = Long.read(b)
        
        return RpcDropAnswer(req_msg_id=req_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.req_msg_id))
        
        return b.getvalue()