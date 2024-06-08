
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



class RpcResult(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RpcResult`.

    Details:
        - Layer: ``181``
        - ID: ``F35C6D01``

req_msg_id (``int`` ``64-bit``):
                    N/A
                
        result (Any object from :obj:`~typegram.api.types`):
                    N/A
                
    """

    __slots__: List[str] = ["req_msg_id", "result"]

    ID = 0xf35c6d01
    QUALNAME = "types.rpcResult"

    def __init__(self, *, req_msg_id: int, result: Object) -> None:
        
                self.req_msg_id = req_msg_id  # long
        
                self.result = result  # Object

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RpcResult":
        # No flags
        
        req_msg_id = Long.read(b)
        
        result = Object.read(b)
        
        return RpcResult(req_msg_id=req_msg_id, result=result)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.req_msg_id))
        
        b.write(self.result.write())
        
        return b.getvalue()