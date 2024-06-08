
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



class ReplyInlineMarkup(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ReplyMarkup`.

    Details:
        - Layer: ``181``
        - ID: ``48A30254``

rows (List of :obj:`KeyboardButtonRow<typegram.api.ayiin.KeyboardButtonRow>`):
                    N/A
                
    """

    __slots__: List[str] = ["rows"]

    ID = 0x48a30254
    QUALNAME = "types.replyInlineMarkup"

    def __init__(self, *, rows: List["api.ayiin.KeyboardButtonRow"]) -> None:
        
                self.rows = rows  # KeyboardButtonRow

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyInlineMarkup":
        # No flags
        
        rows = Object.read(b)
        
        return ReplyInlineMarkup(rows=rows)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.rows))
        
        return b.getvalue()