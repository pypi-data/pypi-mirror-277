
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



class UpdateStoryID(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``1BF335B9``

id (``int`` ``32-bit``):
                    N/A
                
        random_id (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["id", "random_id"]

    ID = 0x1bf335b9
    QUALNAME = "types.updateStoryID"

    def __init__(self, *, id: int, random_id: int) -> None:
        
                self.id = id  # int
        
                self.random_id = random_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStoryID":
        # No flags
        
        id = Int.read(b)
        
        random_id = Long.read(b)
        
        return UpdateStoryID(id=id, random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.id))
        
        b.write(Long(self.random_id))
        
        return b.getvalue()