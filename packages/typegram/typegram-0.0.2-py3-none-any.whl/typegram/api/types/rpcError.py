
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



class RpcError(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RpcError`.

    Details:
        - Layer: ``181``
        - ID: ``2144CA19``

error_code (``int`` ``32-bit``):
                    N/A
                
        error_message (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["error_code", "error_message"]

    ID = 0x2144ca19
    QUALNAME = "types.rpcError"

    def __init__(self, *, error_code: int, error_message: str) -> None:
        
                self.error_code = error_code  # int
        
                self.error_message = error_message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RpcError":
        # No flags
        
        error_code = Int.read(b)
        
        error_message = String.read(b)
        
        return RpcError(error_code=error_code, error_message=error_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.error_code))
        
        b.write(String(self.error_message))
        
        return b.getvalue()