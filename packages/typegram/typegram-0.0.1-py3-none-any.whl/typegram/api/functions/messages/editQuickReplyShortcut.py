
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



class EditQuickReplyShortcut(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``5C003CEF``

shortcut_id (``int`` ``32-bit``):
                    N/A
                
        shortcut (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["shortcut_id", "shortcut"]

    ID = 0x5c003cef
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, shortcut_id: int, shortcut: str) -> None:
        
                self.shortcut_id = shortcut_id  # int
        
                self.shortcut = shortcut  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditQuickReplyShortcut":
        # No flags
        
        shortcut_id = Int.read(b)
        
        shortcut = String.read(b)
        
        return EditQuickReplyShortcut(shortcut_id=shortcut_id, shortcut=shortcut)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.shortcut_id))
        
        b.write(String(self.shortcut))
        
        return b.getvalue()