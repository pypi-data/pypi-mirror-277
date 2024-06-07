
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



class ReorderPinnedSavedDialogs(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8B716587``

order (List of :obj:`InputDialogPeer<typegram.api.ayiin.InputDialogPeer>`):
                    N/A
                
        force (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["order", "force"]

    ID = 0x8b716587
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, order: List["ayiin.InputDialogPeer"], force: Optional[bool] = None) -> None:
        
                self.order = order  # InputDialogPeer
        
                self.force = force  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderPinnedSavedDialogs":
        
        flags = Int.read(b)
        
        force = True if flags & (1 << 0) else False
        order = Object.read(b)
        
        return ReorderPinnedSavedDialogs(order=order, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.order))
        
        return b.getvalue()