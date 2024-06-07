
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



class ReceivedMessages(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``5A954C0``

max_id (``int`` ``32-bit``):
                    N/A
                
    Returns:
        List of :obj:`ReceivedNotifyMessage<typegram.api.ayiin.ReceivedNotifyMessage>`
    """

    __slots__: List[str] = ["max_id"]

    ID = 0x5a954c0
    QUALNAME = "functions.functions.Vector<ReceivedNotifyMessage>"

    def __init__(self, *, max_id: int) -> None:
        
                self.max_id = max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReceivedMessages":
        # No flags
        
        max_id = Int.read(b)
        
        return ReceivedMessages(max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.max_id))
        
        return b.getvalue()