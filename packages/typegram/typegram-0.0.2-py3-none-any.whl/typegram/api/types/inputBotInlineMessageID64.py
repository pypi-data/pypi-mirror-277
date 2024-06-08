
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



class InputBotInlineMessageID64(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBotInlineMessageID`.

    Details:
        - Layer: ``181``
        - ID: ``B6D915D7``

dc_id (``int`` ``32-bit``):
                    N/A
                
        owner_id (``int`` ``64-bit``):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["dc_id", "owner_id", "id", "access_hash"]

    ID = 0xb6d915d7
    QUALNAME = "types.inputBotInlineMessageID64"

    def __init__(self, *, dc_id: int, owner_id: int, id: int, access_hash: int) -> None:
        
                self.dc_id = dc_id  # int
        
                self.owner_id = owner_id  # long
        
                self.id = id  # int
        
                self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageID64":
        # No flags
        
        dc_id = Int.read(b)
        
        owner_id = Long.read(b)
        
        id = Int.read(b)
        
        access_hash = Long.read(b)
        
        return InputBotInlineMessageID64(dc_id=dc_id, owner_id=owner_id, id=id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.dc_id))
        
        b.write(Long(self.owner_id))
        
        b.write(Int(self.id))
        
        b.write(Long(self.access_hash))
        
        return b.getvalue()