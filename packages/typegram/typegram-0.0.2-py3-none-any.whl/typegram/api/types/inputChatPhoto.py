
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



class InputChatPhoto(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputChatPhoto`.

    Details:
        - Layer: ``181``
        - ID: ``8953AD37``

id (:obj:`InputPhoto<typegram.api.ayiin.InputPhoto>`):
                    N/A
                
    """

    __slots__: List[str] = ["id"]

    ID = 0x8953ad37
    QUALNAME = "types.inputChatPhoto"

    def __init__(self, *, id: "api.ayiin.InputPhoto") -> None:
        
                self.id = id  # InputPhoto

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChatPhoto":
        # No flags
        
        id = Object.read(b)
        
        return InputChatPhoto(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        return b.getvalue()