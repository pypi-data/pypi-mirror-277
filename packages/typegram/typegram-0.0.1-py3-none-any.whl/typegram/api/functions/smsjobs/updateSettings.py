
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



class UpdateSettings(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``93FA0BF``

allow_international (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["allow_international"]

    ID = 0x93fa0bf
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, allow_international: Optional[bool] = None) -> None:
        
                self.allow_international = allow_international  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSettings":
        
        flags = Int.read(b)
        
        allow_international = True if flags & (1 << 0) else False
        return UpdateSettings(allow_international=allow_international)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()