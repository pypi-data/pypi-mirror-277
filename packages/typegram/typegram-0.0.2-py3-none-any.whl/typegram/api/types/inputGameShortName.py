
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



class InputGameShortName(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputGame`.

    Details:
        - Layer: ``181``
        - ID: ``C331E80A``

bot_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        short_name (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["bot_id", "short_name"]

    ID = 0xc331e80a
    QUALNAME = "types.inputGameShortName"

    def __init__(self, *, bot_id: "api.ayiin.InputUser", short_name: str) -> None:
        
                self.bot_id = bot_id  # InputUser
        
                self.short_name = short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGameShortName":
        # No flags
        
        bot_id = Object.read(b)
        
        short_name = String.read(b)
        
        return InputGameShortName(bot_id=bot_id, short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot_id.write())
        
        b.write(String(self.short_name))
        
        return b.getvalue()