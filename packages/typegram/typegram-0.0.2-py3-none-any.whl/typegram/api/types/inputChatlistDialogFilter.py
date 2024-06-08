
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



class InputChatlistDialogFilter(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputChatlist`.

    Details:
        - Layer: ``181``
        - ID: ``F3E0DA33``

filter_id (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["filter_id"]

    ID = 0xf3e0da33
    QUALNAME = "types.inputChatlistDialogFilter"

    def __init__(self, *, filter_id: int) -> None:
        
                self.filter_id = filter_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChatlistDialogFilter":
        # No flags
        
        filter_id = Int.read(b)
        
        return InputChatlistDialogFilter(filter_id=filter_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.filter_id))
        
        return b.getvalue()