
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



class InputQuickReplyShortcut(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputQuickReplyShortcut`.

    Details:
        - Layer: ``181``
        - ID: ``24596D41``

shortcut (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["shortcut"]

    ID = 0x24596d41
    QUALNAME = "types.inputQuickReplyShortcut"

    def __init__(self, *, shortcut: str) -> None:
        
                self.shortcut = shortcut  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputQuickReplyShortcut":
        # No flags
        
        shortcut = String.read(b)
        
        return InputQuickReplyShortcut(shortcut=shortcut)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.shortcut))
        
        return b.getvalue()