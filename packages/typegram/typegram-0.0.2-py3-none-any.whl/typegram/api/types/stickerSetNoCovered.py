
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



class StickerSetNoCovered(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StickerSetCovered`.

    Details:
        - Layer: ``181``
        - ID: ``77B15D1C``

set (:obj:`StickerSet<typegram.api.ayiin.StickerSet>`):
                    N/A
                
    Functions:
        This object can be returned by 19 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getAttachedStickers
    """

    __slots__: List[str] = ["set"]

    ID = 0x77b15d1c
    QUALNAME = "types.stickerSetNoCovered"

    def __init__(self, *, set: "api.ayiin.StickerSet") -> None:
        
                self.set = set  # StickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSetNoCovered":
        # No flags
        
        set = Object.read(b)
        
        return StickerSetNoCovered(set=set)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.set.write())
        
        return b.getvalue()