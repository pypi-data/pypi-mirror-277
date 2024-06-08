
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



class InputStickerSetShortName(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputStickerSet`.

    Details:
        - Layer: ``181``
        - ID: ``861CC8A0``

short_name (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["short_name"]

    ID = 0x861cc8a0
    QUALNAME = "types.inputStickerSetShortName"

    def __init__(self, *, short_name: str) -> None:
        
                self.short_name = short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetShortName":
        # No flags
        
        short_name = String.read(b)
        
        return InputStickerSetShortName(short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.short_name))
        
        return b.getvalue()