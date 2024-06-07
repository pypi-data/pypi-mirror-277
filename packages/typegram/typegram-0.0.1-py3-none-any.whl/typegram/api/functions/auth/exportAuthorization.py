
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



class ExportAuthorization(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E5BFFFCD``

dc_id (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`auth.ExportedAuthorization<typegram.api.ayiin.auth.ExportedAuthorization>`
    """

    __slots__: List[str] = ["dc_id"]

    ID = 0xe5bfffcd
    QUALNAME = "functions.functionsauth.ExportedAuthorization"

    def __init__(self, *, dc_id: int) -> None:
        
                self.dc_id = dc_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportAuthorization":
        # No flags
        
        dc_id = Int.read(b)
        
        return ExportAuthorization(dc_id=dc_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.dc_id))
        
        return b.getvalue()