
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



class DeleteQuickReplyMessages(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E105E910``

shortcut_id (``int`` ``32-bit``):
                    N/A
                
        id (List of ``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["shortcut_id", "id"]

    ID = 0xe105e910
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, shortcut_id: int, id: List[int]) -> None:
        
                self.shortcut_id = shortcut_id  # int
        
                self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteQuickReplyMessages":
        # No flags
        
        shortcut_id = Int.read(b)
        
        id = Object.read(b, Int)
        
        return DeleteQuickReplyMessages(shortcut_id=shortcut_id, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.shortcut_id))
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()