
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



class SavedDialogsNotModified(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.SavedDialogs`.

    Details:
        - Layer: ``181``
        - ID: ``C01F6FE8``

count (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 32 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getSavedDialogs
    """

    __slots__: List[str] = ["count"]

    ID = 0xc01f6fe8
    QUALNAME = "types.messages.savedDialogsNotModified"

    def __init__(self, *, count: int) -> None:
        
                self.count = count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedDialogsNotModified":
        # No flags
        
        count = Int.read(b)
        
        return SavedDialogsNotModified(count=count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        return b.getvalue()