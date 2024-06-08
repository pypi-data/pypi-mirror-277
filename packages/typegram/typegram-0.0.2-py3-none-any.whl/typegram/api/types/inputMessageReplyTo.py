
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



class InputMessageReplyTo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputMessage`.

    Details:
        - Layer: ``181``
        - ID: ``BAD88395``

id (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["id"]

    ID = 0xbad88395
    QUALNAME = "types.inputMessageReplyTo"

    def __init__(self, *, id: int) -> None:
        
                self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessageReplyTo":
        # No flags
        
        id = Int.read(b)
        
        return InputMessageReplyTo(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.id))
        
        return b.getvalue()