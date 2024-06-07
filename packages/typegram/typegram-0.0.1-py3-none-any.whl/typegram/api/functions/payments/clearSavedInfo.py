
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



class ClearSavedInfo(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D83D70C1``

credentials (``bool``, *optional*):
                    N/A
                
        info (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["credentials", "info"]

    ID = 0xd83d70c1
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, credentials: Optional[bool] = None, info: Optional[bool] = None) -> None:
        
                self.credentials = credentials  # true
        
                self.info = info  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ClearSavedInfo":
        
        flags = Int.read(b)
        
        credentials = True if flags & (1 << 0) else False
        info = True if flags & (1 << 1) else False
        return ClearSavedInfo(credentials=credentials, info=info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()