
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



class InputWallPaperSlug(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputWallPaper`.

    Details:
        - Layer: ``181``
        - ID: ``72091C80``

slug (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["slug"]

    ID = 0x72091c80
    QUALNAME = "types.inputWallPaperSlug"

    def __init__(self, *, slug: str) -> None:
        
                self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWallPaperSlug":
        # No flags
        
        slug = String.read(b)
        
        return InputWallPaperSlug(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.slug))
        
        return b.getvalue()