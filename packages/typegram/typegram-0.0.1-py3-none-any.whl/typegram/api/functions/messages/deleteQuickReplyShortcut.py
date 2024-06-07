
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



class DeleteQuickReplyShortcut(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3CC04740``

shortcut_id (``int`` ``32-bit``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["shortcut_id"]

    ID = 0x3cc04740
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, shortcut_id: int) -> None:
        
                self.shortcut_id = shortcut_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteQuickReplyShortcut":
        # No flags
        
        shortcut_id = Int.read(b)
        
        return DeleteQuickReplyShortcut(shortcut_id=shortcut_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.shortcut_id))
        
        return b.getvalue()