
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



class Timezone(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Timezone`.

    Details:
        - Layer: ``181``
        - ID: ``FF9289F5``

id (``str``):
                    N/A
                
        name (``str``):
                    N/A
                
        utc_offset (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["id", "name", "utc_offset"]

    ID = 0xff9289f5
    QUALNAME = "types.timezone"

    def __init__(self, *, id: str, name: str, utc_offset: int) -> None:
        
                self.id = id  # string
        
                self.name = name  # string
        
                self.utc_offset = utc_offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Timezone":
        # No flags
        
        id = String.read(b)
        
        name = String.read(b)
        
        utc_offset = Int.read(b)
        
        return Timezone(id=id, name=name, utc_offset=utc_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.id))
        
        b.write(String(self.name))
        
        b.write(Int(self.utc_offset))
        
        return b.getvalue()