
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



class UpdateDialogFilter(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``1AD4A04A``

id (``int`` ``32-bit``):
                    N/A
                
        filter (:obj:`DialogFilter<typegram.api.ayiin.DialogFilter>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "filter"]

    ID = 0x1ad4a04a
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, id: int, filter: "ayiin.DialogFilter" = None) -> None:
        
                self.id = id  # int
        
                self.filter = filter  # DialogFilter

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDialogFilter":
        
        flags = Int.read(b)
        
        id = Int.read(b)
        
        filter = Object.read(b) if flags & (1 << 0) else None
        
        return UpdateDialogFilter(id=id, filter=filter)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        if self.filter is not None:
            b.write(self.filter.write())
        
        return b.getvalue()