
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



class DropTempAuthKeys(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8E48A188``

except_auth_keys (List of ``int`` ``64-bit``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["except_auth_keys"]

    ID = 0x8e48a188
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, except_auth_keys: List[int]) -> None:
        
                self.except_auth_keys = except_auth_keys  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DropTempAuthKeys":
        # No flags
        
        except_auth_keys = Object.read(b, Long)
        
        return DropTempAuthKeys(except_auth_keys=except_auth_keys)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.except_auth_keys, Long))
        
        return b.getvalue()