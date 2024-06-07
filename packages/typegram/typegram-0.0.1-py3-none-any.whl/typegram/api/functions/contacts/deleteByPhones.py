
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



class DeleteByPhones(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``1013FD9E``

phones (List of ``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phones"]

    ID = 0x1013fd9e
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, phones: List[str]) -> None:
        
                self.phones = phones  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteByPhones":
        # No flags
        
        phones = Object.read(b, String)
        
        return DeleteByPhones(phones=phones)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.phones, String))
        
        return b.getvalue()