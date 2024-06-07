
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



class GetTimezonesList(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``49B30240``

hash (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`help.TimezonesList<typegram.api.ayiin.help.TimezonesList>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x49b30240
    QUALNAME = "functions.functionshelp.TimezonesList"

    def __init__(self, *, hash: int) -> None:
        
                self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTimezonesList":
        # No flags
        
        hash = Int.read(b)
        
        return GetTimezonesList(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        return b.getvalue()