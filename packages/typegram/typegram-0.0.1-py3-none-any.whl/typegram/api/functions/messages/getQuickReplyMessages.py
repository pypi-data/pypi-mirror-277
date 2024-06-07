
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



class GetQuickReplyMessages(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``94A495C3``

shortcut_id (``int`` ``32-bit``):
                    N/A
                
        hash (``int`` ``64-bit``):
                    N/A
                
        id (List of ``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.Messages<typegram.api.ayiin.messages.Messages>`
    """

    __slots__: List[str] = ["shortcut_id", "hash", "id"]

    ID = 0x94a495c3
    QUALNAME = "functions.functionsmessages.Messages"

    def __init__(self, *, shortcut_id: int, hash: int, id: Optional[List[int]] = None) -> None:
        
                self.shortcut_id = shortcut_id  # int
        
                self.hash = hash  # long
        
                self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetQuickReplyMessages":
        
        flags = Int.read(b)
        
        shortcut_id = Int.read(b)
        
        id = Object.read(b, Int) if flags & (1 << 0) else []
        
        hash = Long.read(b)
        
        return GetQuickReplyMessages(shortcut_id=shortcut_id, hash=hash, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.shortcut_id))
        
        if self.id is not None:
            b.write(Vector(self.id, Int))
        
        b.write(Long(self.hash))
        
        return b.getvalue()