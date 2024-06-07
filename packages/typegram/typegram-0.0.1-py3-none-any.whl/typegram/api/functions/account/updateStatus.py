
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



class UpdateStatus(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``6628562C``

offline (``bool``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["offline"]

    ID = 0x6628562c
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, offline: bool) -> None:
        
                self.offline = offline  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStatus":
        # No flags
        
        offline = Bool.read(b)
        
        return UpdateStatus(offline=offline)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bool(self.offline))
        
        return b.getvalue()