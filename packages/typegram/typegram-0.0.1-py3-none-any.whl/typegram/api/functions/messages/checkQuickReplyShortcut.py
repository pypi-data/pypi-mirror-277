
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



class CheckQuickReplyShortcut(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F1D0FBD3``

shortcut (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["shortcut"]

    ID = 0xf1d0fbd3
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, shortcut: str) -> None:
        
                self.shortcut = shortcut  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckQuickReplyShortcut":
        # No flags
        
        shortcut = String.read(b)
        
        return CheckQuickReplyShortcut(shortcut=shortcut)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.shortcut))
        
        return b.getvalue()