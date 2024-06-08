
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



class InputQuickReplyShortcutId(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputQuickReplyShortcut`.

    Details:
        - Layer: ``181``
        - ID: ``1190CF1``

shortcut_id (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["shortcut_id"]

    ID = 0x1190cf1
    QUALNAME = "types.inputQuickReplyShortcutId"

    def __init__(self, *, shortcut_id: int) -> None:
        
                self.shortcut_id = shortcut_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputQuickReplyShortcutId":
        # No flags
        
        shortcut_id = Int.read(b)
        
        return InputQuickReplyShortcutId(shortcut_id=shortcut_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.shortcut_id))
        
        return b.getvalue()