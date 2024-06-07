
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



class ReorderPinnedDialogs(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3B1ADF37``

folder_id (``int`` ``32-bit``):
                    N/A
                
        order (List of :obj:`InputDialogPeer<typegram.api.ayiin.InputDialogPeer>`):
                    N/A
                
        force (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["folder_id", "order", "force"]

    ID = 0x3b1adf37
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, folder_id: int, order: List["ayiin.InputDialogPeer"], force: Optional[bool] = None) -> None:
        
                self.folder_id = folder_id  # int
        
                self.order = order  # InputDialogPeer
        
                self.force = force  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderPinnedDialogs":
        
        flags = Int.read(b)
        
        force = True if flags & (1 << 0) else False
        folder_id = Int.read(b)
        
        order = Object.read(b)
        
        return ReorderPinnedDialogs(folder_id=folder_id, order=order, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.folder_id))
        
        b.write(Vector(self.order))
        
        return b.getvalue()