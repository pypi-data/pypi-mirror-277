
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



class CheckGiftCode(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8E51B4C1``

slug (``str``):
                    N/A
                
    Returns:
        :obj:`payments.CheckedGiftCode<typegram.api.ayiin.payments.CheckedGiftCode>`
    """

    __slots__: List[str] = ["slug"]

    ID = 0x8e51b4c1
    QUALNAME = "functions.functionspayments.CheckedGiftCode"

    def __init__(self, *, slug: str) -> None:
        
                self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckGiftCode":
        # No flags
        
        slug = String.read(b)
        
        return CheckGiftCode(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.slug))
        
        return b.getvalue()