
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



class PhotoSizeEmpty(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PhotoSize`.

    Details:
        - Layer: ``181``
        - ID: ``E17E23C``

type (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["type"]

    ID = 0xe17e23c
    QUALNAME = "types.photoSizeEmpty"

    def __init__(self, *, type: str) -> None:
        
                self.type = type  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotoSizeEmpty":
        # No flags
        
        type = String.read(b)
        
        return PhotoSizeEmpty(type=type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.type))
        
        return b.getvalue()