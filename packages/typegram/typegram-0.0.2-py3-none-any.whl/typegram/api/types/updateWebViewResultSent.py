
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



class UpdateWebViewResultSent(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``1592B79D``

query_id (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["query_id"]

    ID = 0x1592b79d
    QUALNAME = "types.updateWebViewResultSent"

    def __init__(self, *, query_id: int) -> None:
        
                self.query_id = query_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateWebViewResultSent":
        # No flags
        
        query_id = Long.read(b)
        
        return UpdateWebViewResultSent(query_id=query_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.query_id))
        
        return b.getvalue()