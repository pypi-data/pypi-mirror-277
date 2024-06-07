
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



class DeleteMessages(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E58E95D2``

id (List of ``int`` ``32-bit``):
                    N/A
                
        revoke (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.AffectedMessages<typegram.api.ayiin.messages.AffectedMessages>`
    """

    __slots__: List[str] = ["id", "revoke"]

    ID = 0xe58e95d2
    QUALNAME = "functions.functionsmessages.AffectedMessages"

    def __init__(self, *, id: List[int], revoke: Optional[bool] = None) -> None:
        
                self.id = id  # int
        
                self.revoke = revoke  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteMessages":
        
        flags = Int.read(b)
        
        revoke = True if flags & (1 << 0) else False
        id = Object.read(b, Int)
        
        return DeleteMessages(id=id, revoke=revoke)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()