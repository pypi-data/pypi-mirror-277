
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



class StickerSetInstallResultArchive(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.StickerSetInstallResult`.

    Details:
        - Layer: ``181``
        - ID: ``35E410A8``

sets (List of :obj:`StickerSetCovered<typegram.api.ayiin.StickerSetCovered>`):
                    N/A
                
    Functions:
        This object can be returned by 39 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.installStickerSet
    """

    __slots__: List[str] = ["sets"]

    ID = 0x35e410a8
    QUALNAME = "types.messages.stickerSetInstallResultArchive"

    def __init__(self, *, sets: List["api.ayiin.StickerSetCovered"]) -> None:
        
                self.sets = sets  # StickerSetCovered

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSetInstallResultArchive":
        # No flags
        
        sets = Object.read(b)
        
        return StickerSetInstallResultArchive(sets=sets)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.sets))
        
        return b.getvalue()