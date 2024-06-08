
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



class InputMessageCallbackQuery(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputMessage`.

    Details:
        - Layer: ``181``
        - ID: ``ACFA1A7E``

id (``int`` ``32-bit``):
                    N/A
                
        query_id (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["id", "query_id"]

    ID = 0xacfa1a7e
    QUALNAME = "types.inputMessageCallbackQuery"

    def __init__(self, *, id: int, query_id: int) -> None:
        
                self.id = id  # int
        
                self.query_id = query_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessageCallbackQuery":
        # No flags
        
        id = Int.read(b)
        
        query_id = Long.read(b)
        
        return InputMessageCallbackQuery(id=id, query_id=query_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.id))
        
        b.write(Long(self.query_id))
        
        return b.getvalue()